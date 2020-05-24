def resolve():
    n, a, b, c = map(int, input().split())
    ll = [int(input()) for _ in range(n)]

    def dfs(cnt, x, y, z):
        if cnt == n:
            if x == 0 or y == 0 or z == 0:
                return float('INF')
            return abs(a - x) + abs(b - y) + abs(c - z) - 30
        r0 = dfs(cnt + 1, x, y, z)
        r1 = dfs(cnt + 1, x + ll[cnt], y, z) + 10
        r2 = dfs(cnt + 1, x, y + ll[cnt], z) + 10
        r3 = dfs(cnt + 1, x, y, z + ll[cnt]) + 10
        return min(r0, r1, r2, r3)

    print(dfs(0, 0, 0, 0))


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
        input = """5 100 90 80
98
40
30
21
80"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 100 90 80
100
100
90
90
90
80
80
80"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 1000 800 100
300
333
400
444
500
555
600
666"""
        output = """243"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
