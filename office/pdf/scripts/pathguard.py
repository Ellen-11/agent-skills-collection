"""Path confinement for command-line arguments.

Hardening patch applied on top of the upstream skill scripts: these tools
parse untrusted documents and take file paths from argv, so every path
argument is validated and fully resolved before any file is opened.

Rules enforced:
- reject NUL / newline / CR injection in arguments
- input paths must exist, must not be a symlink, and (optionally) must
  be a directory
- output paths are resolved up front and their parent directory must
  already exist, so nothing is written through a symlinked ancestor
"""

import sys
from pathlib import Path


def safe_arg_path(raw, *, must_exist=False, must_be_dir=False, kind="path"):
    if not isinstance(raw, str) or not raw or "\x00" in raw or "\n" in raw or "\r" in raw:
        print(f"Error: invalid {kind}: {raw!r}", file=sys.stderr)
        sys.exit(1)

    raw_path = Path(raw)

    if must_exist:
        if not raw_path.exists():
            print(f"Error: {kind} not found: {raw}", file=sys.stderr)
            sys.exit(1)
        if raw_path.is_symlink():
            print(f"Error: {kind} must not be a symlink: {raw}", file=sys.stderr)
            sys.exit(1)
        if must_be_dir and not raw_path.is_dir():
            print(f"Error: {kind} must be a directory: {raw}", file=sys.stderr)
            sys.exit(1)

    resolved = raw_path.resolve()

    if not must_exist and not resolved.parent.is_dir():
        print(
            f"Error: parent directory of {kind} does not exist: {resolved.parent}",
            file=sys.stderr,
        )
        sys.exit(1)

    return resolved
