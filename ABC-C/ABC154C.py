def resolve():
    n = int(input())
    al = list(map(int, input().split()))
    if len(al) == len(set(al)):
        print('YES')
    else:
        print('NO')


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
        input = """5
2 6 1 4 5"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
4 1 3 1 6 2"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
10000000 10000000"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
