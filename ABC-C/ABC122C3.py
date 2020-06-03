def resolve():
    n, q = map(int, input().split())
    sss = list(input())
    cnt = [0] * n
    for i in range(1, n):
        if sss[i - 1] == 'A' and sss[i] == 'C':
            cnt[i] += cnt[i - 1] + 1
        else:
            cnt[i] += cnt[i - 1]

    for _ in range(q):
        li, ri = map(int, input().split())
        print(cnt[ri-1] - cnt[li-1])


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
