def resolve():
    n, m = map(int, input().split())
    abs = [list(map(int, input().split())) for _ in range(n)]
    abs_sorted = sorted(abs, key=lambda x: x[0])
    num = 0
    ans = 0
    while m != 0:
        a, b = abs_sorted[num][0], abs_sorted[num][1]
        if m >= b:
            ans += a * b
            m -= b
            num += 1
        else:
            ans += a * m
            m = 0
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
        input = """2 5
4 9
2 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 30
6 18
2 5
3 10
7 9"""
        output = """130"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100000
1000000000 100000"""
        output = """100000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
