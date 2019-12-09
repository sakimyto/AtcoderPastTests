def resolve():
    x, y = map(int, input().split())
    a = (2 * y - x) / 3
    b = (2 * x - y) / 3

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    mod = 10 ** 9 + 7
    N = 10 ** 6
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    if a.is_integer() and b.is_integer():
        a = int(a)
        c = int(a + b)
        print(cmb(c, a, mod))
    else:
        print(0)

    # import math
    # x, y = map(int, input().split())
    # a = (2 * y - x) / 3
    # b = (2 * x - y) / 3
    # ans = 0
    # if a.is_integer() and b.is_integer():
    #     m = math.factorial(a + b)
    #     n = math.factorial(a) * math.factorial(b)
    #     ans = m // n
    #     ans %= 10 ** 9 + 7
    # print(ans)


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
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999 999999"""
        output = """151840682"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
