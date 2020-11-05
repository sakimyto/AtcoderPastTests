def resolve():
    n = int(input())
    xxx = list(map(lambda x: abs(int(x)), input().split()))
    print(sum(xxx))
    print(sum(x ** 2 for x in xxx) ** 0.5)
    print(max(xxx))


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
2 -1"""
        output = """3
2.236067977499790
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
3 -1 -4 1 -5 9 2 -6 5 -3"""
        output = """39
14.387494569938159
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
