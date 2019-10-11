def resolve():
    a, b, t = map(int, input().split())
    time = 0
    cnt = 0
    while time + a < (t + 0.5):
        cnt += b
        time += a
    print(cnt)


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
        input = """3 5 7"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 9"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 20 19"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
