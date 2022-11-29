import steganowh as cwh
import unittest

# TODO: Figure out how to move this to another direectory

TestCase = unittest.TestCase


class TestCeasar(TestCase):
    """Tests for the Caesar Ciper method."""

    def test_encryption(self):
        """Test encryption."""
        self.assertEquals(cwh.Caesar("bananabread", shift=13).encrypt(), "onananoernq")


if __name__ == "__main__":
    unittest.main()
