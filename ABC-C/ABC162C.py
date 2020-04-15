def resolve():
    # from math import gcd
    # k = int(input())
    # gcd_2 = []
    # ans = 0
    # for a in range(1, k + 1):
    #     for b in range(1, k + 1):
    #         gcd_2.append(gcd(a, b))
    # for ab in gcd_2:
    #     for c in range(1, k + 1):
    #         ans += gcd(ab, c)
    # print(ans)

    # 上記の処理では下記と結局処理量かわらん感
    from math import gcd
    k = int(input())
    ans = 0
    for a in range(1, k + 1):
        for b in range(1, k + 1):
            ab = gcd(a, b)
            for c in range(1, k + 1):
                ans += gcd(ab, c)
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
        input = """2"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """200"""
        output = """10813692"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
