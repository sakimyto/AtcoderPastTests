def resolve():
    n, c = map(int, input().split())
    cnt = [[0 for _ in range(10 ** 5 + 1)] for _ in range(c)]

    for _ in range(n):
        s, t, _c = map(int, input().split())
        for j in range(s, t + 1):
            cnt[_c - 1][j] = 1
    ans = 0
    for i in range(10 ** 5 + 1):
        ans = max(ans, sum(cnt[j][i] for j in range(c)))
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
        input = """3 2
1 7 2
7 8 1
8 12 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
1 3 2
3 4 4
1 4 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 4
56 60 4
33 37 2
89 90 3
32 43 1
67 68 3
49 51 3
31 32 3
70 71 1
11 12 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 4
2 4 2
2 5 3
4 6 2
1 2 1
1 2 2
1 2 3
1 2 4
"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
