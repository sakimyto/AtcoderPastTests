def resolve():
    import numpy as np
    n, t = map(int, input().split())
    lst = np.full((t), -float("inf"))
    lst[0] = 0
    ans = 0
    ab = [list(map(int, input().split())) for i in range(n)]
    ab.sort()
    for a, b in ab:
        ans = max(ans, max(lst) + b)
        if a < t:
            lst[a:] = np.maximum(lst[a:], lst[:-a] + b)
    ans = int(ans)
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
        input = """2 60
10 10
100 100"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 60
10 10
10 20
10 30"""
        output = """60"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 60
30 10
30 20
30 30"""
        output = """50"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 100
15 23
20 18
13 17
24 12
18 29
19 27
23 21
18 20
27 15
22 25"""
        output = """145"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
