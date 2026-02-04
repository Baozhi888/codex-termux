#[cfg(not(target_os = "android"))]
use anyhow::Result;
#[cfg(not(target_os = "android"))]
use clap::Parser;
#[cfg(not(target_os = "android"))]
use codex_network_proxy::Args;
#[cfg(not(target_os = "android"))]
use codex_network_proxy::NetworkProxy;

#[cfg(target_os = "android")]
fn main() {
    eprintln!("codex-network-proxy is not supported on Android/Termux.");
}

#[cfg(not(target_os = "android"))]
#[tokio::main]
async fn main() -> Result<()> {
    tracing_subscriber::fmt::init();

    let args = Args::parse();
    let _ = args;
    let proxy = NetworkProxy::builder().build().await?;
    proxy.run().await?.wait().await
}
