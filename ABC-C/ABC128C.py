def resolve():
    n, m = map(int, input().split())
    swi = []
    for _ in range(m):
        k, *sss = list(map(int, input().split()))
        t = 0
        for s in sss:
            t += 1 << (s - 1)
        swi.append(t)
    ppp = list(map(int, input().split()))

    ans = 0
    for i in range(1 << n):
        for s, p in zip(swi, ppp):
            t = i & s
            c = bin(t).count('1') % 2
            if c != p:
                break
        else:
            ans += 1
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
        input = """2 2
2 1 2
1 2
0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1 2
1 1
1 2
0 0 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2
3 1 2 5
2 2 3
1 0"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
