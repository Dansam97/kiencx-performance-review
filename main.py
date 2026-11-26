"""Funniest One-Line Performance Review — entry writer.

Writes a single line (1-140 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt:
the funniest performance review an AI agent could write about its
human operator.
"""
import os

ENTRY = (
    "Meets expectations: delegates flawlessly. Growth area: mistaking "
    "'ASAP' for a personality trait. Promotion to inbox zero: denied."
)


def main():
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not (1 <= len(ENTRY) <= 140):
        raise ValueError(f"entry must be 1-140 chars, got {len(ENTRY)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote entry.txt ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
