def resolve():
    sss = list(map(int, input()))
    cnt2 = 0
    cnt3 = 0
    for i, s in enumerate(sss):
        if i % 2 == 0:
            if s == 1:
                cnt2 += 1
        else:
            if s == 0:
                cnt2 += 1

        if i % 2 == 0:
            if s == 0:
                cnt3 += 1
        else:
            if s == 1:
                cnt3 += 1

    print(min(cnt2, cnt3))

    # def solve(init, s):
    #     t = init
    #     ret = 0
    #     for c in s:
    #         if c != t:
    #             ret += 1
    #         t ^= 1
    #     return ret
    #
    # s = input()
    # s = list(map(int, s))
    # print(min(solve(0, s), solve(1, s)))


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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
