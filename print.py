from pathlib import Path

root = Path(".")  # change to your folder
include_exts = {".md", ".py", ".html"}  # add ".scss", ".yml", etc. if you want

# Tune these for your repo
ignore_dirs = {
    ".git", "_site", ".jekyll-cache", ".sass-cache", "node_modules", "__pycache__",
    ".pytest_cache", ".mypy_cache", ".venv", "venv", "dist", "build",
    # common altair / export / artifacts folders (edit as needed)
    "altair", "altair_export", "altair_exports", "exports", "export", "figures", "charts", "assets_generated"
}

ignore_file_exts = {".json", ".csv", ".parquet", ".arrow"}  # often huge/auto-generated
max_bytes = 200_000  # 200 KB; raise/lower as desired


def is_ignored(path: Path) -> bool:
    # ignore if any directory component is in ignore_dirs
    if any(part in ignore_dirs for part in path.parts):
        return True
    # ignore certain extensions
    if path.suffix.lower() in ignore_file_exts:
        return True
    return False


for p in sorted(root.rglob("*")):
    if not p.is_file():
        continue
    if is_ignored(p):
        continue
    if p.suffix.lower() not in include_exts:
        continue

    try:
        size = p.stat().st_size
    except OSError:
        continue

    if size > max_bytes:
        rel = p.relative_to(root)
        print("\n" + "=" * 80)
        print(f"FILE: {rel}  (SKIPPED: {size} bytes > {max_bytes})")
        print("=" * 80)
        continue

    rel = p.relative_to(root)
    print("\n" + "=" * 80)
    print(f"FILE: {rel}  ({size} bytes)")
    print("=" * 80)
    try:
        print(p.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        print(p.read_text(encoding="utf-8", errors="replace"))
