def resolve():
    # n = int(input())
    # aaa = list(map(int, input().split()))
    # mod = 1000000007
    # acc = [0] * n
    # acc[n - 1] = aaa[n - 1]
    # ans = 0
    # for i in range(n - 2, 0, -1):
    #     acc[i] = (acc[i + 1] + aaa[i]) % mod
    # for i in range(n - 1):
    #     ans += aaa[i] * acc[i + 1] % mod
    #     ans %= mod
    # print(ans)

    # 全体からひく
    n = int(input())
    aaa = list(map(int, input().split()))
    mod = 1000000007
    ans = 0
    for a in aaa:
        ans += a
        ans %= mod
    ans **= 2
    ans %= mod
    for a in aaa:
        ans -= a ** 2 % mod
        if ans < 0:
            ans += mod
    ans *= pow(2, -1, mod)
    ans %= mod
    print(int(ans))

    # 前から累積和
    # n = int(input())
    # aaa = list(map(int, input().split()))
    # mod = 1000000007
    # acc = [0] * n
    # acc[0] = aaa[0]
    # ans = 0
    # for i in range(1, n):
    #     acc[i] = (aaa[i] % mod + acc[i - 1] % mod) % mod
    # for i in range(n):
    #     ans += ((aaa[i] % mod) * (acc[n - 1] - acc[i])) % mod
    #     ans %= mod
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
