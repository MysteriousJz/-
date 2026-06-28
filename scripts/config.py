"""Configuration settings for hexagram processing scripts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "output"
DEFAULT_LOG_DIR = REPO_ROOT / "logs"

UNIHAN_FILE_CANDIDATES = {
    "readings": [
        REPO_ROOT / "Unihan_Readings.txt",
    ],
    "dictionary_like": [
        REPO_ROOT / "Unihan_DictionaryLikeData.txt",
    ],
}

SECTION_NUMBERS = {
    "判斷辭": 1,
    "彖傳": 2,
    "象傳": 3,
    "爻辭": 4,
    "文言": 5,
    "京氏易傳": 6,
    "周易注": 7,
    "焦氏易林": 8,
}

SECTION_ORDER = [
    "判斷辭",
    "彖傳",
    "象傳",
    "爻辭",
    "文言",
    "京氏易傳",
    "周易注",
    "焦氏易林",
]

SECTION_TITLES = {
    "判斷辭": "一、判斷辭",
    "彖傳": "二、彖傳",
    "象傳": "三、象傳",
    "爻辭": "四、爻辭",
    "文言": "五、文言",
    "京氏易傳": "六、京氏易傳",
    "周易注": "七、周易注",
    "焦氏易林": "八、焦氏易林",
}


@dataclass(frozen=True)
class PrintLayout:
    """Print layout and font hierarchy for final output."""

    page_size: str = "letter"
    margin_top: str = "0.75in"
    margin_right: str = "0.5in"
    margin_bottom: str = "0.75in"
    margin_left: str = "0.75in"

    section_1_2_chinese: str = "24pt"
    section_1_2_pinyin: str = "16pt"

    section_3_7_chinese: str = "20pt"
    section_3_7_pinyin: str = "14pt"

    section_8_chinese: str = "18pt"
    section_8_pinyin: str = "12pt"

    glossary_char: str = "28pt"
    glossary_pinyin: str = "14pt"
    glossary_definition: str = "12pt"
    glossary_locations: str = "10pt"


PRINT_LAYOUT = PrintLayout()


def resolve_source_file(repo_root: Path, hexagram_number: int) -> Path:
    """Resolve source Phase-2 HTML file path for a given hexagram number."""
    candidates = sorted(
        repo_root.glob(f"hexagram_{hexagram_number:02d}_*.html"),
        key=lambda p: p.name,
    )
    filtered = [p for p in candidates if "with_glossary" not in p.name]
    if filtered:
        return filtered[0]
    if candidates:
        return candidates[0]
    raise FileNotFoundError(
        f"No source HTML found for hexagram {hexagram_number:02d} in {repo_root}"
    )
