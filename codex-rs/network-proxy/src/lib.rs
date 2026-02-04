#![deny(clippy::print_stdout, clippy::print_stderr)]

#[cfg(target_os = "android")]
mod android_stub;
#[cfg(target_os = "android")]
pub use android_stub::*;

#[cfg(not(target_os = "android"))]
mod admin;
#[cfg(not(target_os = "android"))]
mod config;
#[cfg(not(target_os = "android"))]
mod http_proxy;
#[cfg(not(target_os = "android"))]
mod network_policy;
#[cfg(not(target_os = "android"))]
mod policy;
#[cfg(not(target_os = "android"))]
mod proxy;
#[cfg(not(target_os = "android"))]
mod reasons;
#[cfg(not(target_os = "android"))]
mod responses;
#[cfg(not(target_os = "android"))]
mod runtime;
#[cfg(not(target_os = "android"))]
mod socks5;
#[cfg(not(target_os = "android"))]
mod state;
#[cfg(not(target_os = "android"))]
mod upstream;

#[cfg(not(target_os = "android"))]
use anyhow::Result;
#[cfg(not(target_os = "android"))]
pub use network_policy::NetworkDecision;
#[cfg(not(target_os = "android"))]
pub use network_policy::NetworkPolicyDecider;
#[cfg(not(target_os = "android"))]
pub use network_policy::NetworkPolicyRequest;
#[cfg(not(target_os = "android"))]
pub use network_policy::NetworkPolicyRequestArgs;
#[cfg(not(target_os = "android"))]
pub use network_policy::NetworkProtocol;
#[cfg(not(target_os = "android"))]
pub use proxy::Args;
#[cfg(not(target_os = "android"))]
pub use proxy::NetworkProxy;
#[cfg(not(target_os = "android"))]
pub use proxy::NetworkProxyBuilder;
#[cfg(not(target_os = "android"))]
pub use proxy::NetworkProxyHandle;

#[cfg(not(target_os = "android"))]
pub async fn run_main(args: Args) -> Result<()> {
    let _ = args;
    let proxy = NetworkProxy::builder().build().await?;
    proxy.run().await?.wait().await
}
