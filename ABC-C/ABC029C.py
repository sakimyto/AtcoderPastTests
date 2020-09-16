def resolve():
    from itertools import product
    n = int(input())
    abcs = list(product(['a', 'b', 'c'], repeat=n))
    for i in abcs:
        print(''.join(i))

    # 再帰関数でも書けるようにする
    # n = int(input())
    #
    # def defs(s):
    #     if len(s) == n:
    #         print(s)
    #         return
    #     defs(s + 'a')
    #     defs(s + 'b')
    #     defs(s + 'c')
    #
    # defs('')


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
        input = """1"""
        output = """a
b
c"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """2"""
        output = """aa
ab
ac
ba
bb
bc
ca
cb
cc"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
