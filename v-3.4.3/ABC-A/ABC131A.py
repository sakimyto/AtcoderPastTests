def resolve():
    s = list(input())
    if s[0] == s[1] or s[1] == s[2] or s[2] == s[3]:
        print("Bad")
    else:
        print("Good")


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
        input = """3776"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8080"""
        output = """Good"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1333"""
        output = """Bad"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """0024"""
        output = """Bad"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
