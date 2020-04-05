def resolve():
    n, k = map(int, input().split())
    ans1 = n % k
    ans2 = abs(ans1 - k)
    print(min(ans1, ans2))


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
        input = """7 4"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
