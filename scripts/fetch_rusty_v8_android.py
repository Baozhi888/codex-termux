#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
import tomllib
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REPOSITORY = "DioNanos/codex-termux"
DEFAULT_TARGET = "aarch64-linux-android"


def resolved_v8_crate_version() -> str:
    cargo_lock = tomllib.loads((ROOT / "codex-rs" / "Cargo.lock").read_text())
    versions = sorted(
        {
            package["version"]
            for package in cargo_lock["package"]
            if package["name"] == "v8"
        }
    )
    if len(versions) != 1:
        raise SystemExit(f"expected exactly one resolved v8 version, found: {versions}")
    return versions[0]


def download(url: str, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url) as response, destination.open("wb") as output:
        shutil.copyfileobj(response, output)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch fork-owned rusty_v8 Android artifacts for Cargo builds."
    )
    parser.add_argument(
        "--repository",
        default=DEFAULT_REPOSITORY,
        help=f"GitHub repository that publishes rusty_v8 artifacts (default: {DEFAULT_REPOSITORY})",
    )
    parser.add_argument(
        "--target",
        default=DEFAULT_TARGET,
        help=f"Rust target triple to fetch (default: {DEFAULT_TARGET})",
    )
    parser.add_argument(
        "--release-tag",
        help="Optional release tag. Defaults to rusty-v8-v<resolved_v8_version>.",
    )
    parser.add_argument(
        "--output-dir",
        default=str(ROOT / ".artifacts" / "rusty_v8"),
        help="Directory where the archive and binding will be stored.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    version = resolved_v8_crate_version()
    release_tag = args.release_tag or f"rusty-v8-v{version}"
    output_dir = Path(args.output_dir).resolve()

    archive_name = f"librusty_v8_release_{args.target}.a.gz"
    binding_name = f"src_binding_release_{args.target}.rs"

    base_url = (
        f"https://github.com/{args.repository}/releases/download/{release_tag}"
    )
    archive_url = f"{base_url}/{archive_name}"
    binding_url = f"{base_url}/{binding_name}"

    archive_path = output_dir / release_tag / archive_name
    binding_path = output_dir / release_tag / binding_name

    try:
        download(archive_url, archive_path)
        download(binding_url, binding_path)
    except urllib.error.HTTPError as exc:
        raise SystemExit(
            "failed to download fork-owned rusty_v8 Android artifacts; "
            f"missing asset or tag: {exc.url} ({exc.code})"
        ) from exc
    except urllib.error.URLError as exc:
        raise SystemExit(f"failed to download rusty_v8 Android artifacts: {exc}") from exc

    print(f"resolved v8 crate version: {version}")
    print(f"release tag: {release_tag}")
    print(f"archive: {archive_path}")
    print(f"archive sha256: {sha256(archive_path)}")
    print(f"binding: {binding_path}")
    print(f"binding sha256: {sha256(binding_path)}")
    print()
    print(f'export RUSTY_V8_ARCHIVE="{archive_path}"')
    print(f'export RUSTY_V8_SRC_BINDING_PATH="{binding_path}"')
    return 0


if __name__ == "__main__":
    sys.exit(main())
