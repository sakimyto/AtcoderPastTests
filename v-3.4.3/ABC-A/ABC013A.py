def resolve():
    x = input()
    l = ['A', 'B', 'C', 'D', 'E']
    for i in range(5):
        if l[i] == x:
            print(i + 1)


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
        input = """A"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """B"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """C"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """D"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
