def resolve():
    n, k, m = map(int, input().split())
    al = list(map(int, input().split()))
    num = m * n - sum(al)
    if num <= 0:
        print(0)
    elif num <= k:
        print(num)
    else:
        print(-1)

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
        input = """5 10 7
8 10 3 6"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100 60
100 100 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 100 60
0 0 0"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
