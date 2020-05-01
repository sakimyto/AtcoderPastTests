def resolve():
    s = input()
    print(*[s.count(x) for x in 'ABCDEF'])


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
        input = """BEAF"""
        output = """1 1 0 0 1 1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """DECADE"""
        output = """1 0 1 2 2 0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """ABBCCCDDDDEEEEEFFFFFF"""
        output = """1 2 3 4 5 6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
