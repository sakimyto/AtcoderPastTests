def resolve():
    a, b, x = map(int, input().split())
    ans = 0
    for d in range(1, 18):
        if b * d > x:
            continue
        upper = 10 ** d
        n = (x - (b * d)) // a
        if n < upper:
            ans = max(ans, n)
    ans = min(ans, 10 ** 9)
    print(ans)


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
        input = """10 7 100"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 100000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1234 56789 314159265"""
        output = """254309"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
