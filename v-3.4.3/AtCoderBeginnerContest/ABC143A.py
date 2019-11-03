def resolve():
    a, b = map(int, input().split())
    print(a - b * 2 if a > b * 2 else 0)

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
        input = """12 4"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """20 15"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """20 30"""
        output = """0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
