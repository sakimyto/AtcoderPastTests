def resolve():
    n = int(input())
    l = list(map(int, input().split()))
    if max(l) * 2 < sum(l):
        print('Yes')
    else:
        print('No')


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
3 8 5 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3 8 4 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
1 8 10 5 8 12 34 100 11 3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
