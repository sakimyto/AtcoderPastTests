def resolve():
    x, y = map(int, input().split())
    print(x if x > y else y)


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
        input = """10 11"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000000 10000000"""
        output = """100000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
