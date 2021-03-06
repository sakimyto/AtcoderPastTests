def resolve():
    from itertools import accumulate

    def primes(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * 2, n + 1, i):
                is_prime[j] = False
        return is_prime

    p_list = primes(10 ** 5)
    cnt = [0] * (10 ** 5 + 2)
    for i in range(1, (10 ** 5 + 1), 2):
        if p_list[i] and p_list[(i + 1) // 2]:
            cnt[i] += 1
    cnt_sum = list(accumulate(cnt))

    q = int(input())
    for _ in range(q):
        li, ri = map(int, input().split())
        print(cnt_sum[ri] - cnt_sum[li - 1])


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
        input = """1
3 7"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
13 13
7 11
7 11
2017 2017"""
        output = """1
0
0
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 53
13 91
37 55
19 51
73 91
13 49"""
        output = """4
4
1
1
1
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
