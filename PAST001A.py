def resolve():
    try:
        print(int(input()) * 2)
    except:
        print('error')


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
        input = """678"""
        output = """1356"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abc"""
        output = """error"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0x8"""
        output = """error"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """012"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
