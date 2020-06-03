def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    right = 0
    sum = 0
    cnt = 0
    for left in range(n):
        while right < n and (sum ^ aaa[right]) == (sum + aaa[right]):
            sum += aaa[right]
            right += 1
        cnt += right - left
        if left == right:
            right += 1
        else:
            sum -= aaa[left]
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

    def test_入力例_1(self):
        input = """4
2 5 4 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
0 0 0 0 0 0 0 0 0"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19
885 8 1 128 83 32 256 206 639 16 4 128 689 32 8 64 885 969 1"""
        output = """37"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
