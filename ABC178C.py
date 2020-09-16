def resolve():
    n = int(input())
    mod = 1000000007
    if n < 2:
        print(0)
    else:
        print((pow(10, n, mod) - 2 * pow(9, n, mod) + pow(8, n, mod)) % mod)


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
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """869121"""
        output = """2511445"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
