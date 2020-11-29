def resolve():
    sx, sy, gx, gy = map(int, input().split())
    print((sx * gy + gx * sy) / (sy + gy))


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
        input = """1 1 7 2"""
        output = """3.0000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 3 2"""
        output = """1.6666666667"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-9 99 -999 9999"""
        output = """-18.7058823529"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
