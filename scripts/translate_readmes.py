import os
import re
from pathlib import Path

from deep_translator import GoogleTranslator


ROOT = Path(__file__).resolve().parents[1]
SOURCE_FILE = ROOT / "README.ja.md"
TARGETS = {
    "en": ROOT / "README.en.md",
    "zh-CN": ROOT / "README.zh-CN.md",
}


TRANSLATE_RE = re.compile(r"[一-龠ぁ-んァ-ン]")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]+\)")


def should_translate(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if stripped.startswith("[日本語]("):
        return False
    if stripped.startswith("```"):
        return False
    return bool(TRANSLATE_RE.search(stripped))


def mask_tokens(text: str):
    tokens = []

    def replacer(match):
        idx = len(tokens)
        tokens.append(match.group(0))
        return f"__TOKEN_{idx}__"

    masked = INLINE_CODE_RE.sub(replacer, text)
    masked = LINK_RE.sub(replacer, masked)
    return masked, tokens


def unmask_tokens(text: str, tokens):
    result = text
    for idx, token in enumerate(tokens):
        result = result.replace(f"__TOKEN_{idx}__", token)
    return result


def translate_line(line: str, target_lang: str) -> str:
    masked, tokens = mask_tokens(line.rstrip("\n"))
    translated = GoogleTranslator(source="ja", target=target_lang).translate(masked)
    if translated is None:
        translated = masked
    restored = unmask_tokens(translated, tokens)
    return restored + "\n"


def translate_file(target_lang: str, out_file: Path):
    lines = SOURCE_FILE.read_text(encoding="utf-8").splitlines(keepends=True)
    output_lines = []
    in_code_block = False

    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            output_lines.append(line)
            continue

        if in_code_block or not should_translate(line):
            output_lines.append(line)
            continue

        output_lines.append(translate_line(line, target_lang))

    out_file.write_text("".join(output_lines), encoding="utf-8")


def sync_readme_md():
    content = SOURCE_FILE.read_text(encoding="utf-8")
    (ROOT / "README.md").write_text(content, encoding="utf-8")


def main():
    if not SOURCE_FILE.exists():
        raise FileNotFoundError("README.ja.md not found.")

    sync_readme_md()
    for lang, out_file in TARGETS.items():
        translate_file(lang, out_file)

    print("Translated README files generated successfully.")


if __name__ == "__main__":
    main()
