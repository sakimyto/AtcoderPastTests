def resolve():
    import itertools
    import collections
    n = int(input())
    aaa = list(map(int, input().split()))
    cnt = [0] * n
    cnt[0] = aaa[0]
    for i in range(1, n):
        cnt[i] = cnt[i - 1] + aaa[i]
    cnt = [0] + cnt
    num_cnt = collections.Counter(cnt)
    ans = 0
    for num in num_cnt.most_common():
        if num[1] != 1:
            ans += num[1] * (num[1] - 1) // 2
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
        input = """6
1 3 -4 2 2 -2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 -1 1 -1 1 -1 1"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 -2 3 -4 5"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
