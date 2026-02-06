from pathlib import Path

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
root = Path(".")  # repository root

# Where to save the log (Windows)
output_dir = Path(r"C:\Users\fiory\Desktop\logs")
output_file = output_dir / "repo_dump.txt"

# Content rules
include_exts = {".md", ".py", ".html"}
ignore_dirs = {
    ".git", "_site", ".jekyll-cache", ".sass-cache", "node_modules", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".venv", "venv", "dist", "build",
    "altair", "altair_export", "altair_exports", "exports", "export",
    "figures", "charts", "assets_generated",
}
ignore_file_exts = {".json", ".csv", ".parquet", ".arrow"}

# Size / truncation
max_bytes = 200_000            # skip content if file > this many bytes
max_lines_per_file = 20        # None = no line limit
max_chars_per_file = 1000      # None = no char limit (THIS fixes minified 1-line files)
max_total_lines = 50_000       # None = no global line limit (prevents gigantic logs)


# --------------------------------------------------
# HELPERS
# --------------------------------------------------
def is_ignored(path: Path) -> bool:
    if any(part in ignore_dirs for part in path.parts):
        return True
    if path.suffix.lower() in ignore_file_exts:
        return True
    return False


def write_file_block(f, p: Path, allow_content: bool, state: dict):
    """
    Writes one file entry to the output.
    state: {"total_lines": int, "stop": bool}
    """
    if state.get("stop"):
        return

    try:
        size = p.stat().st_size
    except OSError:
        return

    rel = p.relative_to(root)

    def writeln(s: str = ""):
        if state.get("stop"):
            return
        f.write(s + "\n")
        state["total_lines"] += 1
        if max_total_lines is not None and state["total_lines"] >= max_total_lines:
            f.write("\n=== STOP: reached max_total_lines ===\n")
            state["stop"] = True

    writeln("=" * 80)
    writeln(f"FILE: {rel}  ({size} bytes)")
    writeln("=" * 80)

    if not allow_content:
        writeln("(content not written)")
        return

    if size > max_bytes:
        writeln(f"(SKIPPED: {size} bytes > {max_bytes})")
        return

    # Counters for truncation
    chars_written = 0
    lines_written = 0

    def write_text_piece(text: str):
        """Write text with per-file char cap."""
        nonlocal chars_written
        if state.get("stop"):
            return False

        if max_chars_per_file is None:
            f.write(text)
            chars_written += len(text)
            return True

        remaining = max_chars_per_file - chars_written
        if remaining <= 0:
            return False

        if len(text) <= remaining:
            f.write(text)
            chars_written += len(text)
            return True

        # truncate this piece
        f.write(text[:remaining])
        chars_written += remaining
        return False

    try:
        with p.open("r", encoding="utf-8", errors="replace") as src:
            for line in src:
                if state.get("stop"):
                    break

                # Enforce line limit (logical lines)
                if max_lines_per_file is not None and lines_written >= max_lines_per_file:
                    writeln(f"... (truncated after {max_lines_per_file} lines)")
                    break

                # Prefix to make it obvious how many lines were written
                prefix = (
                    f"[LINE {lines_written + 1}/{max_lines_per_file}] "
                    if max_lines_per_file is not None
                    else ""
                )

                # Try to write prefix + line, but respect char cap
                ok = write_text_piece(prefix + line)
                if not (prefix + line).endswith("\n"):
                    # ensure newline separation in log
                    ok2 = write_text_piece("\n")
                    ok = ok and ok2

                lines_written += 1
                state["total_lines"] += 1

                # Global line limit
                if max_total_lines is not None and state["total_lines"] >= max_total_lines:
                    f.write("\n=== STOP: reached max_total_lines ===\n")
                    state["stop"] = True
                    break

                # Per-file char cap reached
                if not ok:
                    writeln(f"\n... (truncated after {max_chars_per_file} characters)")
                    break

    except OSError:
        writeln("(error reading file)")


# --------------------------------------------------
# MAIN
# --------------------------------------------------
output_dir.mkdir(parents=True, exist_ok=True)
state = {"total_lines": 0, "stop": False}

with output_file.open("w", encoding="utf-8", newline="\n") as f:

    # 1) MAIN FOLDER FILES: ALWAYS LIST THEM
    for p in sorted(root.iterdir()):
        if state["stop"]:
            break
        if not p.is_file():
            continue

        allow_content = (not is_ignored(p)) and (p.suffix.lower() in include_exts)
        write_file_block(f, p, allow_content, state)

    # 2) RECURSIVE FILES: ONLY INCLUDED ONES
    for p in sorted(root.rglob("*")):
        if state["stop"]:
            break
        if not p.is_file():
            continue
        if p.parent == root:
            continue  # already handled above
        if is_ignored(p):
            continue
        if p.suffix.lower() not in include_exts:
            continue

        write_file_block(f, p, allow_content=True, state=state)

print(f"Saved log to: {output_file}")
