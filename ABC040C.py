def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    dp = [float('inf')] * n
    dp[0] = 0
    dp[1] = abs(aaa[1] - aaa[0])
    for i in range(2, n):
        step1 = dp[i - 1] + abs(aaa[i] - aaa[i - 1])
        step2 = dp[i - 2] + abs(aaa[i] - aaa[i - 2])
        dp[i] = min(step1, step2)
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

    def test_入力例1(self):
        input = """4
100 150 130 120"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
100 125 80 110"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """9
314 159 265 358 979 323 846 264 338"""
        output = """310"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
