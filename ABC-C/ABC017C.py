def resolve():
    n, m = map(int, input().split())
    cnt = [0] * (m + 2)
    cnt_sum = [0] * (m + 2)
    s_sum = 0
    for _ in range(n):
        l, r, s = map(int, input().split())
        cnt[l] += s
        cnt[r + 1] -= s
        s_sum += s
    for i in range(1, m + 2):
        cnt_sum[i] = cnt_sum[i - 1] + cnt[i]
    print(s_sum - min(cnt_sum[1:m+1]))


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

    def test_入力例1(self):
        input = """4 6
1 3 30
2 3 40
3 6 25
6 6 10"""
        output = """80"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2 7
1 3 90
5 7 90"""
        output = """180"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """1 4
1 4 70"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
