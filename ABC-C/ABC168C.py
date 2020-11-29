def resolve():
    import math
    a, b, h, m = map(int, input().split())
    theta_l = m / 60 * 360
    theta_s = h * 30 + m / 60 * 30
    theta_c = abs(theta_l - theta_s)
    cos_c = math.cos(math.radians(theta_c))
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * cos_c))


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
