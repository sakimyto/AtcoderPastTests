def resolve():
    n, m = map(int, input().split())
    fs_list = [[0] * n for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        fs_list[a - 1][b - 1] = 1
        fs_list[b - 1][a - 1] = 1

    for i in range(n):
        ans = [0] * n
        for j in range(n):
            if fs_list[i][j] == 1:
                for k in range(n):
                    if fs_list[j][k] == 1:
                        ans[k] = 1

        for j in range(n):
            if fs_list[i][j] == 1:
                ans[j] = 0

        ans[i] = 0

        print(sum(ans))


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
        input = """3 2
1 2
2 3"""
        output = """1
0
1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """0
0
0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """8 12
1 6
1 7
1 8
2 5
2 6
3 5
3 6
4 5
4 8
5 6
5 7
7 8"""
        output = """4
4
4
5
2
3
4
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
