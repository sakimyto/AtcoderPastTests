def resolve():
    n, k = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(k)]
    mod = 998244353

    dp = [0] * n
    dp[0] = 1
    acc = 0

    for i in range(1, n):
        for li, ri in lr:
            if i - li >= 0:
                acc += dp[i - li]
                acc %= mod
            if i - ri - 1 >= 0:
                acc -= dp[i - ri - 1]
                acc %= mod
        dp[i] = acc
    print(dp[-1])


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
        input = """5 2
1 1
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
3 3
5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """60 3
5 8
1 3
10 15"""
        output = """221823067"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
