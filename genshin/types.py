"""Types used in the library."""
import enum


class Region(str, enum.Enum):
    """Region to get data from."""

    OVERSEAS = "os"
    """Applies to all overseas APIs."""

    CHINESE = "cn"
    """Applies to all chinese mainland APIs."""


class Game(str, enum.Enum):
    """Hoyoverse game."""

    GENSHIN = "genshin"
    """Genshin Impact"""

    HONKAI = "honkai3rd"
    """Honkai Impact 3rd"""
