def resolve():
    a, b = map(str, input().split())
    print(int(a + b) * 2)


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
        input = """1 23"""
        output = """246"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """999 999"""
        output = """1999998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
