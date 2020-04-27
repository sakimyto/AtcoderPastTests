def resolve():
    n, m = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    cd = [list(map(int, input().split())) for _ in range(m)]
    for i in range(n):
        seq_min = 1e9
        ans = -1
        for j in range(m):
            seq = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
            if seq_min > seq:
                seq_min = seq
                ans = j
        print(ans + 1)


if __name__ == '__resolve__':
    resolve()

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
        input = """2 2
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
