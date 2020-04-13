def resolve():
    # TLE
    # n = int(input())
    # s = input()
    # r_list = []
    # g_list = []
    # b_list = []
    # cnt = 0
    # for i, j in enumerate(s):
    #     if j == 'R':
    #         r_list.append(i)
    #     if j == 'G':
    #         g_list.append(i)
    #     if j == 'B':
    #         b_list.append(i)
    # for r in r_list:
    #     for g in g_list:
    #         for b in b_list:
    #             if not (r * 2 == g + b or g * 2 == r + b or b * 2 == r + g):
    #                 cnt += 1
    # print(cnt)

    n = int(input())
    s = input()

    r_cnt = s.count('R')
    g_cnt = s.count('G')
    b_cnt = s.count('B')

    ans = r_cnt * g_cnt * b_cnt

    for i in range(n):
        for d in range(n):
            j = i + d
            k = j + d
            if k >= n:
                break
            if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                ans -= 1
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
        input = """4
RRGB"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB"""
        output = """1800"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
