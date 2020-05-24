def resolve():
    import itertools
    n, q = map(int, input().split())
    s = input()
    cnt = [0] * n
    for i in range(1, n):
        if s[i] == 'C' and s[i - 1] == 'A':
            cnt[i] = 1
    cnt = list(itertools.accumulate(cnt))
    for _ in range(q):
        l, r = map(int, input().split())
        print(cnt[r - 1] - cnt[l - 1])


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
