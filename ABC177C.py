def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    mod = 1000000007
    c_sum = [0] * n
    c_sum[n - 1] = aaa[n - 1]
    ans = 0

    for i in range(n - 2, 0, -1):
        c_sum[i] = (c_sum[i + 1] + aaa[i]) % mod

    for i in range(n - 1):
        ans += aaa[i] * c_sum[i + 1] % mod
        ans %= mod

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
        input = """3
1 2 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
141421356 17320508 22360679 244949"""
        output = """437235829"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
