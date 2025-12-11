import hashlib
from typing import List

def deck_hash(card_ids: List[str]) -> str:
    sorted_ids = sorted(card_ids)
    card_string = "".join(sorted_ids)
    return hashlib.md5(card_string.encode()).hexdigest()[:12]
