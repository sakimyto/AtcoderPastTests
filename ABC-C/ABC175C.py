def resolve():
    x, k, d = map(int, input().split())
    x = abs(x)
    if k * d < x:
        ans = x - k * d
    else:
        if (k - x // d) % 2 == 0:
            ans = x % d
        else:
            ans = abs(x % d - d)
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
        input = """6 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 4 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 1 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000000000000 1000000000000000 1000000000000000"""
        output = """1000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
