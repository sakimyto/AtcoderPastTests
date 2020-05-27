def resolve():
    n = int(input())
    cnt = [0] * 1000002
    cnt_sum = [0] * 1000002
    for _ in range(n):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b + 1] -= 1
    cnt_sum[0] = cnt[0]
    for i in range(1, 1000001):
        cnt_sum[i] = cnt_sum[i - 1] + cnt[i]
    print(max(cnt_sum))


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
        input = """4
0 2
2 3
2 4
5 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1000000 1000000
1000000 1000000
0 1000000
1 1000000"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
