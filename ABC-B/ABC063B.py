def resolve():
    s = input()
    print('yes' if len(s) == len(set(s)) else 'no')


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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """different"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
