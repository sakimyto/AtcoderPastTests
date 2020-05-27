def resolve():
    n, q = map(int, input().split())
    ans = [['N'] * n for _ in range(n)]

    def all_follow(num):
        for i in range(n):
            if ans[i][num] == 'Y':
                ans[num][i] = 'Y'

    def follow_follow(num):
        tmp = []
        for i in range(n):
            if ans[num][i] == 'Y':
                for j in range(n):
                    if ans[i][j] == 'Y':
                        tmp.append(j)
        for i in tmp:
            ans[num][i] = 'Y'

    for _ in range(q):
        f = list(map(int, input().split()))
        if f[0] == 1:
            ans[f[1] - 1][f[2] - 1] = 'Y'
        elif f[0] == 2:
            all_follow(f[1] - 1)
        else:
            follow_follow(f[1] - 1)

    for i in range(n):
        ans[i][i] = 'N'

    for a in ans:
        print(''.join(a))


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
        input = """6 7
1 1 2
1 2 3
1 3 4
1 1 5
1 5 6
3 1
2 6"""
        output = """NYYNYY
NNYNNN
NNNYNN
NNNNNN
NNNNNY
YNNNYN"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
