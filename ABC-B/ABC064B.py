def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    print(max(aaa) - min(aaa))


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
        input = """4
2 3 7 9"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
3 1 4 1 5 9 2 6"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
