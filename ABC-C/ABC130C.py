def resolve():
    w, h, x, y = map(int, input().split())
    if x * 2 == w and y * 2 == h:
        print(w * h / 2, 1)
    else:
        print(w * h / 2, 0)


import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """2 3 1 2"""
        output = """3.000000 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1 1"""
        output = """2.000000 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
