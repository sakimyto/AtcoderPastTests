def resolve():
    # n, w = list(map(int, input().split()))
    # dp = [0] * (w + 1)
    #
    # def ans(n, w):
    #     for _ in range(n):
    #         tmp_w, tmp_v = map(int, input().split())
    #         for j in range(w, tmp_w - 1, -1):
    #             dp[j] = max(dp[j - tmp_w] + tmp_v, dp[j])
    #     return dp[-1]
    #
    # print(ans(n, w))

    n, w = list(map(int, input().split()))
    dp = [0] * (w + 1)
    for _ in range(n):
        tmp_w, tmp_v = map(int, input().split())
        for j in range(w, tmp_w - 1, -1):
            dp[j] = max(dp[j], dp[j - tmp_w] + tmp_v)
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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
