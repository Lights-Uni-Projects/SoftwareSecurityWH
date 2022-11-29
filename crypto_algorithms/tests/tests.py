import cryptowh as cwh
import unittest

# TODO: Figure out how to move this to another direectory

TestCase = unittest.TestCase


class TestCeasar(TestCase):
    def test_encryption(self):
        self.assertEquals(cwh.Caesar("bananabread", shift=13).encrypt(), "onananoernq")


if __name__ == "__main__":
    unittest.main()
