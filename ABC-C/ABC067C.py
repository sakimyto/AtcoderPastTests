def resolve():
    from itertools import accumulate
    n = int(input())
    aaa = list(map(int, input().split()))
    a_sum = list(accumulate(aaa))
    ans = 1e10
    for i in range(n - 1):
        ans = min(ans, abs(a_sum[i] - a_sum[n - 1] + a_sum[i]))
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
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
