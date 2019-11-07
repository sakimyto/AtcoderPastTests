def resolve():


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
        input = """4 3
1 2
2 3
2 4
2 10
1 100
3 1"""
        output = """100 110 111 110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10"""
        output = """20 20 20 20 20 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
