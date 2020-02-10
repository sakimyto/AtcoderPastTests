def resolve():
    # 処理時間が足りない
    # n, k = map(int, input().split())
    # pl = list(map(int, input().split()))
    # pl_i = []
    # pl_max = 0
    # s = 0
    # for i in range(n):
    #     for j in range(1, pl[i]+1):
    #         s += j
    #     pl_i.append(s / pl[i])
    #     s = 0
    # for m in range(n - k + 1):
    #     pl_max = max(pl_max, sum(pl_i[m:m + k]))
    # print(pl_max)

    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    tmp = sum(p[:k])
    res = tmp
    for i in range(n - k):
        tmp -= p[i]
        tmp += p[i + k]
        res = max(res, tmp)
    print((res + k) / 2)


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
        input = """5 3
1 2 2 4 5"""
        output = """7.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
6 6 6 6"""
        output = """3.500000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 4
17 13 13 12 15 20 10 13 17 11"""
        output = """32.000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
