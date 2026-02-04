use std::io;

#[derive(Debug, Default, Clone)]
pub struct Args;

impl Args {
    pub fn parse() -> Self {
        Self
    }
}

#[derive(Debug, Default, Clone)]
pub struct NetworkProxy;

#[derive(Debug, Default, Clone)]
pub struct NetworkProxyBuilder;

#[derive(Debug, Default, Clone)]
pub struct NetworkProxyHandle;

impl NetworkProxy {
    pub fn builder() -> NetworkProxyBuilder {
        NetworkProxyBuilder
    }
}

impl NetworkProxyBuilder {
    pub async fn build(self) -> io::Result<NetworkProxy> {
        Err(io::Error::new(
            io::ErrorKind::Unsupported,
            "codex-network-proxy is not supported on Android/Termux",
        ))
    }
}

impl NetworkProxy {
    pub async fn run(self) -> io::Result<NetworkProxyHandle> {
        Err(io::Error::new(
            io::ErrorKind::Unsupported,
            "codex-network-proxy is not supported on Android/Termux",
        ))
    }
}

impl NetworkProxyHandle {
    pub async fn wait(self) -> io::Result<()> {
        Ok(())
    }
}

pub async fn run_main(_args: Args) -> io::Result<()> {
    Err(io::Error::new(
        io::ErrorKind::Unsupported,
        "codex-network-proxy is not supported on Android/Termux",
    ))
}
