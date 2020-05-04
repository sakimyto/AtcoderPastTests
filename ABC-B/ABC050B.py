def resolve():
    n = int(input())
    ttt = list(map(int, input().split()))
    m = int(input())
    pxs = [list(map(int, input().split())) for _ in range(m)]
    sum_t = sum(ttt)
    for i in range(m):
        print(sum_t - ttt[pxs[i][0] - 1] + pxs[i][1])


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
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
