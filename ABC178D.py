def resolve():
    s = int(input())
    dp = [0] * (s + 11)
    mod = 10 ** 9 + 7
    dp[0] = 1
    dp[1] = 0
    dp[2] = 0
    dp[3] = 1
    c = 2
    for i in range(4, s + 1):
        dp[i] = (c - dp[i - 1] - dp[i - 2]) % mod
        c = (c + dp[i]) % mod
    print(dp[s])


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
        input = """7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1729"""
        output = """294867501"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
