def resolve():
    n = int(input())
    s = input()
    ai = ord('A')
    ans = ''
    for i in s:
        ei = ord(i) - ai
        ei = (ei + n) % 26
        ans += chr(ei + ai)
    print(ans)


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
        input = """2
ABCXYZ"""
        output = """CDEZAB"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0
ABCXYZ"""
        output = """ABCXYZ"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """13
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
        output = """NOPQRSTUVWXYZABCDEFGHIJKLM"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
