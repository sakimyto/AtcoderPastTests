def resolve():
    from fractions import gcd
    # import math #mathにgcdがあるのがpython_v3.5以降
    # import numpy @こちらもnumpy_V1.15.0以降

    def prime_factors(n):
        lst = []
        while n % 2 == 0:
            lst.append(2)
            n //= 2
        while n % 3 == 0:
            lst.append(3)
            n //= 3
        f = 5
        limit = int(n ** .5)
        while f <= limit:
            while n % f == 0:
                lst.append(f)
                n //= f
            f += 2
        if n != 1:
            lst.append(n)
        return lst

    a, b = map(int, input().split())
    print(len(set(prime_factors(gcd(a, b)))) + 1)


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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
