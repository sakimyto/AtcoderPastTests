def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a = sum(a)
    for i in range(n):
        tmp = min(a[i], b[i])
        a[i] -= tmp
        b[i] -= tmp
        tmp = min(a[i + 1], b[i])
        a[i + 1] -= tmp
        b[i] -= tmp
    ans = sum_a - sum(a)
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
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
