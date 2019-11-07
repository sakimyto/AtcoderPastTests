def resolve():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    for i in range(n):
        h[i] = abs(t - h[i] * 0.006 - a)
    print(h.index(min(h)) + 1)


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
        input = """2
12 5
1000 2000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
21 -11
81234 94124 52141"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
