#!/usr/bin/env python3
"""To KV function."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Calculate the values passed."""
    return (k, float(v ** 2))
