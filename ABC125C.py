def resolve():
    def gcd(x, y):
        if y == 0:
            return x
        else:
            return gcd(y, x % y)

    n = int(input())
    aaa = list(map(int, input().split()))
    cnt_l = [0] * (n - 1)
    cnt_r = [0] * (n - 1)

    cnt_l[0] = aaa[0]
    for i in range(1, n - 1):
        cnt_l[i] = gcd(cnt_l[i - 1], aaa[i])

    aaa.reverse()
    cnt_r[0] = aaa[0]
    for i in range(1, n - 1):
        cnt_r[i] = gcd(cnt_r[i - 1], aaa[i])

    cnt_l = [cnt_r[-1]] + cnt_l
    cnt_r = [cnt_l[-1]] + cnt_r
    cnt_r.reverse()

    ans = 1
    for i in range(n):
        tmp = gcd(cnt_l[i], cnt_r[i])
        ans = max(ans, tmp)

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
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """2
4 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """2
12 13"""
        output = """13"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
