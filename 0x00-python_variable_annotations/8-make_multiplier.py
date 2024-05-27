#!/usr/bin/env python3
"""Multiplier Module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        A function that multiplies its input by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the input value by the predefined multiplier.

        Args:
            value (float): The value to be multiplied.

        Returns:
            float: The result of the multiplication.
        """
        return value * multiplier

    return multiplier_function
