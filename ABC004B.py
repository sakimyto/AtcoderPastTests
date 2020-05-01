def resolve():
    ccc = [list(input()) for _ in range(4)]
    for i in range(4):
        print(''.join(ccc[3-i][::-1]))


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
        input = """. . . .
. o o .
. x x .
. . . ."""
        output = """. . . .
. x x .
. o o .
. . . ."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """o o x x
o o x x
x x o o
x x o o"""
        output = """o o x x
o o x x
x x o o
x x o o"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
