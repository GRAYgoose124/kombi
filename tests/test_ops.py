import unittest
from kombi import *


class TestOps(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(identity(5), 5)
        self.assertEqual(identity("test"), "test")

    def test_compose(self):
        f = compose(lambda x: x * 2, lambda x: x + 3)
        self.assertEqual(f(5), 16)  # (5 + 3) * 2

    def test_pipe(self):
        f = pipe(lambda x: x * 2, lambda x: x + 3)
        self.assertEqual(f(5), 13)  # (5 * 2) + 3

    def test_split(self):
        f = split(lambda x: x + 1, lambda x: x * 2)
        self.assertEqual(f(5), (6, 10))

    def test_duplicate(self):
        f = duplicate(lambda x: x + 2)
        self.assertEqual(f(3), (5, 5))

    def test_map1(self):
        f = map1(lambda x: x * 2)
        self.assertEqual(f([1, 2, 3]), [2, 4, 6])

    def test_map2(self):
        f = map2(lambda x: x * 2)
        self.assertEqual(list(f([1, 2, 3])), [2, 4, 6])

    def test_starmap1(self):
        f = starmap1(lambda x, y: x + y)
        self.assertEqual(f([(1, 2), (3, 4)]), [3, 7])

    def test_chain(self):
        self.assertEqual(chain([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_interleave(self):
        self.assertEqual(interleave([1, 2], [3, 4]), [1, 3, 2, 4])


if __name__ == "__main__":
    unittest.main()
