def resolve():
    # n = int(input())
    # aaa = list(map(int, input().split()))
    #
    # now = 0
    # move = 0
    # move_plus = 0
    # ans = 0
    #
    # for ai in aaa:
    #     move += ai
    #     if move > move_plus:
    #         move_plus = move
    #     ans = max(ans, now + move_plus)
    #     now += move
    #
    # print(ans)

    from itertools import accumulate

    n = int(input())
    aaa = list(map(int, input().split()))

    ans = 0
    x = 0

    acc = list(accumulate(aaa))
    acc_max = list(accumulate(acc, func=max))

    for i in range(n):
        ans = max(ans, x + acc_max[i])
        x += acc[i]

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
        input = """3
2 -1 -2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
-2 1 3 -1 -1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
-1000 -1000 -1000 -1000 -1000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
