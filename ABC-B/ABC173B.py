def resolve():
    n = int(input())
    cnt = [0] * 4
    for _ in range(n):
        tmp = input()
        if tmp == 'AC':
            cnt[0] += 1
        elif tmp == 'WA':
            cnt[1] += 1
        elif tmp == 'TLE':
            cnt[2] += 1
        else:
            cnt[3] += 1

    j_txt = ['AC', 'WA', 'TLE', 'RE']

    for i in range(4):
        print(j_txt[i] + ' x ' + str(cnt[i]))


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
        input = """6
AC
TLE
AC
AC
WA
TLE"""
        output = """AC x 3
WA x 1
TLE x 2
RE x 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
AC
AC
AC
AC
AC
AC
AC
AC
AC
AC"""
        output = """AC x 10
WA x 0
TLE x 0
RE x 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
