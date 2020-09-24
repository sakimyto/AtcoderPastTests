def resolve():
    import math
    n, x, t = map(int, input().split())
    print(math.ceil(n / x) * t)


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
        input = """20 12 6"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000 1 1000"""
        output = """1000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
