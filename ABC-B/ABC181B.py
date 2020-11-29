def resolve():
    n = int(input())
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        ans += (b - a + 1) * (a + b) // 2
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
        input = """2
1 3
3 5"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
11 13
17 47
359 44683"""
        output = """998244353"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1 1000000"""
        output = """500000500000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
