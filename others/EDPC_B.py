def resolve():
    # pypyじゃないとTLEになった
    # n, k = map(int, input().split())
    # hhh = list(map(int, input().split()))
    # dp = [float('inf')] * n
    # dp[0] = 0
    # for i in range(1, n):
    #     min_tmp = float('inf')
    #     if i - k >= 0:
    #         for j in range(i - k, i):
    #             tmp = dp[j] + abs(hhh[i] - hhh[j])
    #             min_tmp = min(tmp, min_tmp)
    #         dp[i] = min_tmp
    #     else:
    #         for j in range(i):
    #             tmp = dp[j] + abs(hhh[i] - hhh[j])
    #             min_tmp = min(tmp, min_tmp)
    #         dp[i] = min_tmp
    # print(dp[-1])

    import numpy as np
    n, k = map(int, input().split())
    hhh = np.array(list(map(int, input().split())))
    dp = np.zeros(n, dtype=int)
    for i in range(1, n):
        start = max(0, i - k)
        dp[i] = min(dp[start:i] + np.abs(hhh[i] - hhh[start:i]))
    print(dp[n - 1])


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
10 30 40 50 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
10 20 10"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 100
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4
40 10 20 70 80 10 20 70 80 60"""
        output = """40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
