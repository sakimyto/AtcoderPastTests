def resolve():
    a, b = map(int, input().split())
    print(int(a * b))


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
        input = """2 5"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 100"""
        output = """10000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
