from languages.hebrew import HEBREW
from languages.slovak import SLOVAK

LANG_PACKS = {
    "hebrew": HEBREW,
    "slovak": SLOVAK,
}


def get_lang_pack(name: str):
    if name not in LANG_PACKS:
        raise ValueError(f"Unknown language pack: {name!r}. Available: {list(LANG_PACKS)}")
    return LANG_PACKS[name]
