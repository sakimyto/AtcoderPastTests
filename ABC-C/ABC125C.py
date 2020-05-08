def resolve():
    from fractions import gcd
    n = int(input())
    aaa = list(map(int, input().split()))
    p = aaa[0]
    f = [p]
    for a in aaa[1:-1]:
        p = gcd(p, a)
        f.append(p)
    aaa.reverse()
    p = aaa[0]
    b = [p]
    for a in aaa[1:-1]:
        p = gcd(p, a)
        b.append(p)
    b.reverse()

    f = [b[0]] + f
    b = b + [f[-1]]

    print(max(gcd(p, q) for p, q in zip(f, b)))


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
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
