def resolve():
    abcdef = list(map(int, input().split()))
    abcdef.sort()
    print(abcdef[-3])

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
        input = """4 18 25 20 9 13"""
        output = """18"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """95 96 97 98 99 100"""
        output = """98"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """19 92 3 35 78 1"""
        output = """35"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()