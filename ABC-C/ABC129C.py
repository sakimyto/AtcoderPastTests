def resolve():
    n, m = map(int, input().split())
    p = 1000000007
    aaa = [0] * (n + 1)
    f = [0] * (n + 1)
    for _ in range(m):
        x = int(input())
        aaa[x] = 1
    f[0] = 1
    if aaa[1] == 1:
        f[1] = 0
    else:
        f[1] = 1
    for i in range(2, n + 1):
        f[i] = (f[i - 1] + f[i - 2]) % p
        if aaa[i] == 1:
            f[i] = 0
    print(f[n])


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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
