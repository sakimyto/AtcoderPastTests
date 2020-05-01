def resolve():
    n = int(input())
    mod = 10007
    a1, a2, a3 = 0, 0, 1
    if n < 3:
        ans = 0
    elif n == 3:
        ans = 1
    else:
        for i in range(4, n + 1):
            a1, a2, a3 = a2, a3, (a1 + a2 + a3) % mod
        ans = a3
    print(int(ans))


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
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000"""
        output = """7927"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
