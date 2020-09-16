def resolve():
    s = input()
    if s == 'RRR':
        print(3)
    elif s == 'RRS' or s == 'SRR':
        print(2)
    elif s == 'SSS':
        print(0)
    else:
        print(1)


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
        input = """RRS"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """SSS"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RSR"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
