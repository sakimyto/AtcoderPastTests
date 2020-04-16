def resolve():
    h1, w1 = map(int, input().split())
    h2, w2 = map(int, input().split())
    print('YES' if h1 == h2 or h1 == w2 or w1 == w2 or w1 == h2 else 'NO')


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
        input = """1080 1920
1080 1920"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1080 1920
1920 1080"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """334 668
668 1002"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """100 200
300 150"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """120 120
240 240"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
