def resolve():
    n, k = map(int, input().split())
    sss = [int(input()) for _ in range(n)]
    right = 0
    cnt = 0
    tmp = 1
    for left in range(n):
        while right < n and tmp * sss[right] <= k:
            if sss[right] == 0:
                cnt = n
                break
            tmp *= sss[right]
            right += 1
        cnt = max(cnt, right - left)
        if left == right:
            right += 1
        else:
            tmp /= sss[left]
    print(cnt)


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
        input = """7 6
4
3
1
1
2
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 10
10
10
10
10
0
10"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 9
10
10
10
10
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
