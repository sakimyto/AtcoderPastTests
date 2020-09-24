def resolve():
    # n = int(input())
    # l_list = list(map(int, input().split()))
    # l_list.sort()
    # ans = 0
    #
    # for i in range(len(l_list)):
    #     for j in range(i + 1, len(l_list)):
    #         for k in range(j + 1, len(l_list)):
    #             if l_list[i] + l_list[j] > l_list[k] \
    #                     and l_list[i] != l_list[j] \
    #                     and l_list[j] != l_list[k] \
    #                     and l_list[k] != l_list[i]:
    #                 ans += 1
    # print(ans)

    n = int(input())
    lll = list(map(int, input().split()))
    lll.sort()
    len_lll = len(lll)
    ans = 0
    for i in range(len_lll):
        a = lll[i]
        for j in range(i + 1, len_lll):
            b = lll[j]
            for k in range(j + 1, len_lll):
                c = lll[k]
                if a + b > c and a != b and b != c:
                    ans += 1
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
        input = """5
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
