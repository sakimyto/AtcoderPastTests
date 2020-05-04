def resolve():
    n, t = map(int, input().split())
    aaa = [int(input()) for _ in range(n)]
    ans = 0
    for i in range(n - 1):
        if aaa[i] + t > aaa[i + 1]:
            ans += aaa[i + 1] - aaa[i]
        else:
            ans += t
    print(ans + t)


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
        input = """5 10
20
100
105
217
314"""
        output = """45"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """10 10
1
2
3
4
5
6
7
8
9
10"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """10 100000
3
31
314
3141
31415
314159
400000
410000
500000
777777"""
        output = """517253"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
