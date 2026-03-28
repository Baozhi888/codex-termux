#!/usr/bin/env python3
"""Patch PT_TLS alignment for Android ARM64 executables.

Android's ARM64 Bionic loader rejects executables whose TLS segment alignment is
less than 64 bytes. Some cross-linked binaries still end up with PT_TLS p_align
set to 8, which causes:

    executable's TLS segment is underaligned: alignment is 8, needs to be at
    least 64 for ARM64 Bionic

This utility raises PT_TLS p_align to 64 in-place for 64-bit ELF files when
needed. It intentionally keeps the patch narrow instead of rewriting unrelated
ELF metadata.
"""

from __future__ import annotations

import argparse
import os
import struct
import sys
from pathlib import Path


ELF_MAGIC = b"\x7fELF"
ELFCLASS64 = 2
PT_TLS = 7
MIN_TLS_ALIGN_AARCH64_BIONIC = 64


def patch_file(path: Path, dry_run: bool) -> tuple[bool, int | None]:
    with path.open("r+b") as fh:
        ident = fh.read(16)
        if len(ident) < 16 or ident[:4] != ELF_MAGIC:
            raise ValueError(f"{path}: not an ELF file")
        if ident[4] != ELFCLASS64:
            raise ValueError(f"{path}: only 64-bit ELF is supported")

        fh.seek(32)
        phoff = struct.unpack("<Q", fh.read(8))[0]
        fh.seek(54)
        phentsize = struct.unpack("<H", fh.read(2))[0]
        phnum = struct.unpack("<H", fh.read(2))[0]

        for index in range(phnum):
            entry_offset = phoff + index * phentsize
            fh.seek(entry_offset)
            p_type = struct.unpack("<I", fh.read(4))[0]
            if p_type != PT_TLS:
                continue

            align_offset = entry_offset + 48
            fh.seek(align_offset)
            current_align = struct.unpack("<Q", fh.read(8))[0]
            if current_align >= MIN_TLS_ALIGN_AARCH64_BIONIC:
                return False, current_align

            if not dry_run:
                fh.seek(align_offset)
                fh.write(struct.pack("<Q", MIN_TLS_ALIGN_AARCH64_BIONIC))

            return True, current_align

    return False, None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true", help="inspect only")
    parser.add_argument("files", nargs="+", help="ELF binaries to patch")
    args = parser.parse_args()

    patched_any = False
    for raw in args.files:
        path = Path(raw)
        patched, previous = patch_file(path, dry_run=args.dry_run)
        if previous is None:
            print(f"{path}: no PT_TLS segment found")
            continue
        if patched:
            action = "would patch" if args.dry_run else "patched"
            print(
                f"{path}: {action} PT_TLS p_align {previous} -> "
                f"{MIN_TLS_ALIGN_AARCH64_BIONIC}"
            )
            patched_any = True
        else:
            print(f"{path}: PT_TLS p_align already {previous}")

    return 0 if patched_any or args.dry_run else 0


if __name__ == "__main__":
    sys.exit(main())
