def resolve():
    n = int(input())
    cnt_l = {}
    for _ in range(n):
        a = int(input())
        if a in cnt_l:
            cnt_l[a] ^= 1
        else:
            cnt_l[a] = 1
    print(sum(cnt_l.values()))


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
6
2
6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2
5
5
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
12
22
16
22
18
12"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
