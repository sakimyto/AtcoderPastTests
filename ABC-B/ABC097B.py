def resolve():
    x = int(input())
    m = 1
    for i in range(2, x):
        p = 2
        while pow(i, p) <= x:
            if m <= pow(i, p):
                m = pow(i, p)
            p += 1
    print(m)


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
        input = """10"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999"""
        output = """961"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
