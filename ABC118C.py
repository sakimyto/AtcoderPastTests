def resolve():
    n = int(input())
    a = list(map(int, input().split()))

    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    ans = gcd(a[0], a[1])
    for i in range(2, n):
        ans = gcd(ans, a[i])
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
        input = """4
2 10 8 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 13 8 1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
