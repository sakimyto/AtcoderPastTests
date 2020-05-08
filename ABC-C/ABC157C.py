def resolve():
    def solve(n, m):
        ans = [-1] * n
        for _ in range(m):
            s, c = input().split()
            s = int(s) - 1
            if ans[s] == c:
                continue
            elif ans[s] == -1:
                ans[s] = c
            else:
                return -1

        if ans[0] == '0':
            if n == 1:
                return '0'
            else:
                return -1
        elif ans[0] == -1:
            if n == 1:
                return '0'
            else:
                ans[0] = '1'

        for i in range(1, n):
            if ans[i] == -1:
                ans[i] = '0'
        return ''.join(ans)

    n, m = map(int, input().split())
    print(solve(n, m))


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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
