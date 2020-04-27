def resolve():
    a, b, c = map(int, input().split())
    ans = 'NO'
    for i in range(b):
        if (a * (i + 1)) % b == c:
            ans = 'YES'
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
        input = """7 5 1"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 100 97"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """40 98 58"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """77 42 36"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
