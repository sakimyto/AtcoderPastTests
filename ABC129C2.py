def resolve():
    n, m = map(int, input().split())
    aaa = [0] * (n + 1)
    for _ in range(m):
        aaa[int(input())] = 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if aaa[1] == 1 else 1
    for i in range(2, n + 1):
        if aaa[i] == 1:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[n] % 1000000007)


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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
