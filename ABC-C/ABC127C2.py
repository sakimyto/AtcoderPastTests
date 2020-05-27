def resolve():
    n, m = map(int, input().split())
    cnt = [0] * (n + 2)
    cnt_sum = [0] * (n + 1)
    for _ in range(m):
        l, r = map(int, input().split())
        cnt[l] += 1
        cnt[r + 1] -= 1
    cnt_sum[0] = cnt[0]
    for i in range(1, n + 1):
        cnt_sum[i] = cnt_sum[i - 1] + cnt[i]
    print(cnt_sum.count(m))


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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
