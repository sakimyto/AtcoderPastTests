def resolve():
    n, m = map(int, input().split())
    xxx = sorted(list(map(int, input().split())))
    if n >= m:
        ans = 0
    else:
        ddd = [0] * (m - 1)
        for i in range(m - 1):
            ddd[i] = xxx[i + 1] - xxx[i]
        ddd = sorted(ddd)
        ans = sum(ddd[:m - n])
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
10 12 1 2 14"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 7
-10 -3 0 9 -100 2 17"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1
-100000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
