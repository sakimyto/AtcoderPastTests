def resolve():
    n = int(input())
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60

    print('{:02d}:{:02d}:{:02d}'.format(h, m, s))


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
        input = """3661"""
        output = """01:01:01"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """86399"""
        output = """23:59:59"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
