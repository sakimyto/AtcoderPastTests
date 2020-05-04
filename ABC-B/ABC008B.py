def resolve():
    n = int(input())
    sss = {}
    for _ in range(n):
        tmp = input()
        if tmp in sss:
            sss[tmp] += 1
        else:
            sss[tmp] = 1
    print(max(sss, key=sss.get))


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

    def test_入力例1(self):
        input = """4
taro
jiro
taro
saburo"""
        output = """taro"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1
takahashikun"""
        output = """takahashikun"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """9
a
b
c
c
b
c
b
d
e"""
        output = """b"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
