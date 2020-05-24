def resolve():
    n, q = map(int, input().split())
    s = list(input())
    lrs = [list(map(int, input().split())) for _ in range(q)]
    d = [0] * n
    cnt = 0
    for i in range(n-1):
        if s[i:i + 2] == ['A', 'C']:
            cnt += 1
        d[i+1] = cnt
    for j in range(q):
        l, r = lrs[j][0], lrs[j][1]
        print(d[r - 1] - d[l - 1])


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
        input = """8 3
ACACTACG
3 7
2 3
1 8"""
        output = """2
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
