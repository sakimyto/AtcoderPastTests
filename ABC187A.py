def resolve():
    a, b = input().split()
    print(max(sum(map(int, a)), sum(map(int, b))))


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
        input = """123 234"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """593 953"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 999"""
        output = """27"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
