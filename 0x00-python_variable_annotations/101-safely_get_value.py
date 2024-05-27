#!/usr/bin/env python3
"""Typing with Typevar."""
from typing import TypeVar, Mapping, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping[str, T], key: str, default: Optional[T] = None) -> Optional[T]:
    """
    Safely get a value from a dictionary.

    Args:
        dct (Mapping[str, T]): The dictionary to search.
        key (str): The key to search for.
        The default value to return if the key is not found.

    Returns:
        The value associated otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
