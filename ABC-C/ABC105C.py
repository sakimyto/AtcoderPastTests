def resolve():
    n = int(input())
    ans = ''
    while n != 0:
        if n % (-2) == 0:
            ans = '0' + ans
        else:
            ans = '1' + ans
            n -= 1
        n /= -2
    if ans == '':
        ans = '0'
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
        input = """-9"""
        output = """1011"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789"""
        output = """11000101011001101110100010101"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
