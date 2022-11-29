import re
import warnings
from string import ascii_letters, ascii_lowercase, ascii_uppercase
from time import time
from typing import Any

from .base import SteganographyBase

__all__: list[str] = [
    "Caesar"
]


class Caesar(SteganographyBase):
    """Steganography using the caesar cipher method."""

    input: str
    """Input string."""

    shift: int
    """Amount of alphabetical characters to offset by."""

    def __init__(self, input: str, shift: int = 13, **kwargs: Any):
        """
        Steganography using the Caesar cipher algorithm.

        This works by substituting a character with the Nth character
        in the alphabet, making it a very easy message to break.

        :param input:               The input value to encrypt. Must be a string.
        :param shift:               The amount of alphabetical characters to offset by.
                                    Must be more or less than 0 and less than 25/more than -25.
        :param remove_non_ascii:    If True, remove non-ascii characters. Else, ignore them.
        :param all_caps:            If True, set the entire input string to uppercase.
        """
        super().__init__(**kwargs)

        if not isinstance(input, str):
            raise ValueError("Your input must be a string!")

        if self.remove_non_ascii:
            input = re.sub('[^A-Za-z0-9]+', '', input)

        # Validating `shift`.
        if abs(shift) > (len(ascii_lowercase) - 1):
            raise ValueError("Offset will wrap around the alphabet. "
                             f"Please set is between 1 and {len(ascii_lowercase)}")
        elif shift == 0:
            warnings.warn("Offset is 0! Your message will not be encrypted!")
            shift = False
        else:
            if shift > 13:
                shift -= 13
            elif shift < -13:
                shift += 13

        # Setting values.
        self.input = input
        self.shift = shift

    @staticmethod
    def __algorithm(input: str, shift: int, encrypt: bool) -> str:
        out_str: str = ""

        ascii_upper_a, ascii_lower_a = ascii_uppercase[0], ascii_lowercase[0]

        for char in input:
            if char not in ascii_letters:
                out_str += char
                continue

            ascii_char_get = ascii_lower_a if char.islower() else ascii_upper_a
            ascii_char = ord(ascii_char_get)

            char_index = ord(char) - ascii_char
            char_shift = (char_index + shift) if encrypt else (char_index - shift)
            char_shift = char_shift % len(ascii_lowercase) + ascii_char

            out_str += chr(char_shift)

        return out_str

    def encrypt(self) -> str:
        """
        Encrypt an input string using the Caesar cipher algorithm.

        :return:            Encrypted string.
        """
        if not self.shift:
            return self.input

        return self.__algorithm(self.input, self.shift, encrypt=True)

    def decrypt(self) -> str:
        """
        Decrypt an input string using the Caesar cipher algorithm.

        :return:            Decrypted string.
        """
        if not self.shift:
            return self.input

        return self.__algorithm(self.input, self.shift, encrypt=False)

    def bruteforce(self, timer: bool = True) -> list[str]:
        """
        Bruteforce a Ceasar cypher.

        All the results will be printed in the terminal.

        :param timer:       Whether to time the operation or not.
                            Time taken gets printed at the end of the process.
        """
        if timer:
            start = time()

        results: list[str] = []

        for i in range(1, 26):
            alg = self.__algorithm(self.input, i, encrypt=False)
            results += [alg]

            print(f"Shift by {i}: {alg}")

        if timer:
            end = time()
            print(f"Time taken: {end - start} seconds")

        return results
