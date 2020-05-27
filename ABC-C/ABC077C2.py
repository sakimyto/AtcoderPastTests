def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    bbb = list(map(int, input().split()))
    ccc = list(map(int, input().split()))

    aaa.sort()
    ccc.sort()

    def is_ok_a(mid, b):
        if mid < 0:
            return True
        elif mid >= n:
            return False
        else:
            return aaa[mid] < b

    def m_bisect_a(ng, ok, b):
        while abs(ng - ok) > 1:
            mid = (ng + ok) // 2
            if is_ok_a(mid, b):
                ok = mid
            else:
                ng = mid
        return ok

    def is_ok_c(mid, b):
        if mid < 0:
            return False
        elif mid >= n:
            return True
        else:
            return ccc[mid] > b

    def m_bisect_c(ng, ok, b):
        while abs(ng - ok) > 1:
            mid = (ng + ok) // 2
            if is_ok_c(mid, b):
                ok = mid
            else:
                ng = mid
        return ok

    ans = 0
    for i in range(n):
        b = bbb[i]
        ng, ok = n, -1
        cnt_a = m_bisect_a(ng, ok, b) + 1
        ng, ok = -1, n
        cnt_c = n - m_bisect_c(ng, ok, b)
        ans += (cnt_a * cnt_c)

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
        input = """2
1 5
2 4
3 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 1
2 2 2
3 3 3"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
3 14 159 2 6 53
58 9 79 323 84 6
2643 383 2 79 50 288"""
        output = """87"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
