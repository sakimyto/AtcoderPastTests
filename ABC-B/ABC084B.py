def resolve():
    a, b = map(int, input().split())
    s = input().split('-')
    if len(s) != 2:
        print('No')
    elif len(s[0]) != a or len(s[1]) != b:
        print('No')
    else:
        print('Yes')


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
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()