from abc import ABC, abstractmethod
from typing import Any

__all__: list[str] = [
    "SteganographyBase"
]


class SteganographyBase(ABC):
    """Abstract steganography class."""

    remove_non_ascii: bool
    """Whether to ignore non-ascii characters or remove them."""

    all_caps: bool
    """Whether to convert the cipher to uppercase."""

    def __init__(self, remove_non_ascii: bool = False, all_caps: bool = False) -> None:
        """
        Initiate base steganography class.

        :param remove_non_ascii:    If True, remove non-ascii characters. Else, ignore them.
                                    Default: False.
        :param all_caps:            If True, set the entire cipher to uppercase.
                                    Default: False.
        """
        self.remove_non_ascii = remove_non_ascii
        self.all_caps = all_caps

    @abstractmethod
    def encrypt(self) -> str:
        """Encrypt a cipher using the current encryption algorithm."""
        ...

    @abstractmethod
    def decrypt(self) -> str:
        """Decrypt a cipher using the current encryption algorithm."""
        ...

    @abstractmethod
    def bruteforce(self, timer: bool = True) -> Any:
        """Run a bruteforce algorithm on a given cipher."""
        ...
