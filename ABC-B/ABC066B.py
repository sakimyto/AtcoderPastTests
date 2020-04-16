def resolve():
    s = input()
    ls = len(s)
    for i in range(ls - 2, 0, -2):
        if s[:i // 2] == s[i // 2:i]:
            print(i)
            break


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
        input = """abaababaab"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xxxx"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcabcabcabc"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """akasakaakasakasakaakas"""
        output = """14"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
