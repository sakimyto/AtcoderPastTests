def resolve():
    n = int(input())
    list_c = [9 ** i for i in range(6)]
    list_c += [6 ** i for i in range(1, 7)]
    list_c.sort()

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(n):
        for c in list_c:
            if i + c <= n:
                dp[i + c] = min(dp[i + c], dp[i] + 1)

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
        input = """127"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """44852"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
