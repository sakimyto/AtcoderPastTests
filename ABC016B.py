def resolve():
    a, b, c = map(int, input().split())
    ans_p = a + b
    ans_m = a - b
    if ans_p == c and ans_m == c:
        print('?')
    elif ans_p == c:
        print('+')
    elif ans_m == c:
        print('-')
    else:
        print('!')


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

    def test_入力例1(self):
        input = """1 0 1"""
        output = """?"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1 1 2"""
        output = """+"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 1 0"""
        output = """-"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """1 1 1"""
        output = """!"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
