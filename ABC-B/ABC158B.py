def resolve():
    n, a, b = map(int, input().split())
    ans = n // (a + b) * a
    add = n % (a + b)
    ans += min(add, a)
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
        input = """8 3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 0 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
