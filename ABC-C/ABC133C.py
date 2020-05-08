def resolve():
    a, b, c, d = map(int, input().split())

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    e = lcm(c, d)

    x = b - a + 1
    y = b // c - (a - 1) // c
    z = b // d - (a - 1) // d
    w = b // e - (a - 1) // e

    print(x - y - z + w)


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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
