def resolve():
    n, k = map(int, input().split())
    if n < 10:
        print(k + (100 * (10 - n)))
    else:
        print(k)


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
        input = """2 2919"""
        output = """3719"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """22 3051"""
        output = """3051"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
