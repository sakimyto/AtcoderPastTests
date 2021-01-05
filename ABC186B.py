def resolve():
    h, w = map(int, input().split())
    aaa = [list(map(int, input().split())) for _ in range(h)]
    sum_a = sum(sum(i) for i in aaa)
    min_a = min(min(i) for i in aaa)
    print(sum_a - min_a * h * w)


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
        input = """2 3
2 2 3
3 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
99 99 99
99 0 99
99 99 99"""
        output = """792"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
4 4
4 4
4 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
