def resolve():
    n, a = map(int, input().split())
    x = list(map(int, input().split()))
    max_x = max(max(x), a)
    dp = [[[0] * (n * max_x + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    for i in range(n + 1):
        for j in range(n + 1):
            for k in range(n * max_x + 1):
                if i >= 1 and k < x[i - 1]:
                    dp[i][j][k] = dp[i - 1][j][k]
                elif i >= 1 and j >= 1 and k >= x[i - 1]:
                    dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - 1][k - x[i - 1]]
                else:
                    continue
    ans = 0
    for j in range(1, n + 1):
        ans += dp[n][j][j * a]
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
        input = """4 8
7 9 8 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 8
6 6 9"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 5
3 6 2 8 7 6 5 9"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """33 3
3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3"""
        output = """8589934591"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
