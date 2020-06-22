def resolve():
    n, k = map(int, input().split())
    ppp = list(map(int, input().split()))
    ppp.sort()
    print(sum(ppp[:k]))


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
50 100 80 120 80"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
1000"""
        output = """1000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
