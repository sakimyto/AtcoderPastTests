def resolve():
    import bisect
    n, m, k = map(int, input().split())
    aaa = list(map(int, input().split()))
    bbb = list(map(int, input().split()))
    sum_a = [0] * (n + 1)
    sum_b = [0] * (m + 1)

    for i in range(n):
        sum_a[i + 1] = sum_a[i] + aaa[i]

    for j in range(m):
        sum_b[j + 1] = sum_b[j] + bbb[j]

    ans = 0
    for i in range(n + 1):
        if sum_a[i] > k:
            break
        tmp = bisect.bisect_right(sum_b, k - sum_a[i])
        ans = max(ans, i + tmp - 1)
    print(ans)

    # n, m, k = map(int, input().split())
    # aaa = list(map(int, input().split()))
    # bbb = list(map(int, input().split()))
    # t, ans = sum(bbb), 0
    # j = m
    # for i in range(n + 1):
    #     while j > 0 and t > k:
    #         j -= 1
    #         t -= bbb[j]
    #     if t > k:
    #         break
    #     ans = max(ans, i + j)
    #     if i == n:
    #         break
    #     t += aaa[i]
    # print(ans)


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
        input = """3 4 240
60 90 120
80 150 80 150"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 730
60 90 120
80 150 80 150"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 4 1
1000000000 1000000000 1000000000 1000000000 1000000000
1000000000 1000000000 1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
