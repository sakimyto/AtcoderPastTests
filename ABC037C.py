def resolve():
    n, k = map(int, input().split())
    aaa = list(map(int, input().split()))
    cnt = [0] * n
    cnt[0] = aaa[0]
    for i in range(1, n):
        cnt[i] = cnt[i - 1] + aaa[i]
    cnt = [0] + cnt
    ans = 0
    for i in range((n - k + 1), n+1):
        ans += cnt[i] - cnt[i - (n - k + 1)]
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
        input = """5 3
1 2 4 8 16"""
        output = """49"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999"""
        output = """10988865195"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
