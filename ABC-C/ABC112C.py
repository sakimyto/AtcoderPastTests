def resolve():
    n = int(input())
    xyh = [list(map(int, input().split())) for _ in range(n)]
    xyh.sort(key=lambda x: x[2], reverse=True)
    ans = []

    for cx in range(101):
        for cy in range(101):
            x, y, h = xyh[0]
            ch = h + abs(x - cx) + abs(y - cy)
            if all([h == max(ch - abs(x - cx) - abs(y - cy), 0) for x, y, h in xyh[1:]]):
                ans = [cx, cy, ch]
                break
    print(*ans, sep=' ')


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
2 3 5
2 1 5
1 2 5
3 2 5"""
        output = """2 2 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 0 100
1 1 98"""
        output = """0 0 100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
99 1 191
100 1 192
99 0 192"""
        output = """100 0 193"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
