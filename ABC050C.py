def resolve():
    def pow_mod(n, k, m):
        if k == 0:
            return 1
        if k & 1:
            return (pow_mod(n, k - 1, m) * n % m) % m
        else:
            return (pow_mod(n, k // 2, m) ** 2) % m

    n = int(input())
    aaa = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    aaa.sort()
    if n % 2 == 0:
        for i in range(0, n, 2):
            if aaa[i] != aaa[i + 1]:
                print(0)
                exit()
        print(pow_mod(2, (n // 2), mod))
    else:
        for i in range(1, n, 2):
            if aaa[i] != aaa[i + 1]:
                print(0)
                exit()
        print(pow_mod(2, ((n - 1) // 2), mod))


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
        input = """5
2 4 4 0 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
6 4 0 2 4 0 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
7 5 1 1 7 3 5 3"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
