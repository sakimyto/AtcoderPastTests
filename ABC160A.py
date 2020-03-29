def resolve():
    s = input()
    if s[2] == s[3] and s[4] == s[5]:
        print('Yes')
    else:
        print('No')

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
        input = """sippuu"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """iphone"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """coffee"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()