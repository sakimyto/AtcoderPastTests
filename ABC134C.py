def resolve():
    n = int(input())
    aaa = [int(input()) for i in range(n)]
    max_l = [0] * (n - 1)
    max_r = [0] * (n - 1)
    max_l[0] = aaa[0]
    for i in range(1, n - 1):
        max_l[i] = max(aaa[i], max_l[i - 1])
    max_l = [1] + max_l

    aaa.reverse()
    max_r[0] = aaa[0]
    for i in range(1, n - 1):
        max_r[i] = max(aaa[i], max_r[i - 1])
    max_r = [1] + max_r
    max_r.reverse()

    for i in range(n):
        print(max(max_l[i], max_r[i]))


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
        input = """3
1
4
3"""
        output = """4
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
5
5"""
        output = """5
5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
