def resolve():
    n, k = map(int, input().split())
    lll = list(map(int, input().split()))
    lll.sort()
    print(sum(lll[n - k:n]))


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
        input = """5 3
1 2 3 4 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """15 14
50 26 27 21 41 7 42 35 7 5 5 36 39 1 45"""
        output = """386"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
