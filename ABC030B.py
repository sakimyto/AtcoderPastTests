def resolve():
    n, m = map(int, input().split())
    n = n if n < 12 else n - 12
    ans = abs((m / 60 * 360) - ((n + m / 60) * 30))
    print(ans if ans <= 180 else 360 - ans)


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
        input = """15 0"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 17"""
        output = """3.5"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """0 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6 0"""
        output = """180"""
        self.assertIO(input, output)

    def test_入力例5(self):
        input = """23 59"""
        output = """5.5000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
