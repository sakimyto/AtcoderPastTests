def resolve():
    h1 = int(input())
    h2 = int(input())
    print(h1 - h2)


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
        input = """15
10"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0
0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
20"""
        output = """-15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
