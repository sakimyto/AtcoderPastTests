def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    print(1 / sum(1 / x for x in a))


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
        input = """2
10 30"""
        output = """7.5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
200 200 200"""
        output = """66.66666666666667"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000"""
        output = """1000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
