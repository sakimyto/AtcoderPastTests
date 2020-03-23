def resolve():
    # n = int(input())
    # al = list(map(int, input().split()))
    # al_cnt = [0] * (n + 1)
    #
    # for i in range(1, n + 1):
    #     al_cnt[i] = al.count(i)
    # max_cnt = 0
    #
    # for j in range(1, n + 1):
    #     if al_cnt[j] >= 2:
    #         max_cnt += al_cnt[j] * (al_cnt[j] - 1) / 2
    #
    # for l in range(n):
    #     if al_cnt[al[l]] >= 3:
    #         ans = max_cnt - (al_cnt[al[l]] * (al_cnt[al[l]] - 1) / 2) + ((al_cnt[al[l]] - 1) * (al_cnt[al[l]] - 2) / 2)
    #         print(int(ans) if ans > 0 else 0)
    #     else:
    #         ans = max_cnt - (al_cnt[al[l]] * (al_cnt[al[l]] - 1) / 2)
    #         print(int(ans) if ans > 0 else 0)

    from collections import Counter

    n = int(input())
    al = list(map(int, input().split()))
    al_cnt = Counter(al)
    ans = sum([i * (i - 1) // 2 for i in al_cnt.values()])
    for j in al:
        print(ans - al_cnt[j] + 1)


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
1 1 2 1 2"""
        output = """2
2
3
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
3 3 3 3 3"""
        output = """6
6
6
6
6"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """8
1 2 1 4 2 1 4 1"""
        output = """5
7
5
7
7
5
7
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
