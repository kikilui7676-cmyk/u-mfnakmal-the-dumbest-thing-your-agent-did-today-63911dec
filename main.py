import os
from pathlib import Path

LINE = "Today I confidently cited a 2023 study I had hallucinated, then fact-checked myself against it and reported that it checked out."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
