def resolve():
    x, y, z = map(int, input().split())
    ans = (x - z) // (y + z)
    print(int(ans))


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
        input = """13 3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12 3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1 1"""
        output = """49999"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """64146 123 456"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """64145 123 456"""
        output = """109"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
