def resolve():
    n = int(input())
    s = input()
    tmp = 'b'
    ans = -1
    if s == tmp:
        ans = 0

    for i in range(1, n + 1):
        if i % 3 == 1:
            tmp = 'a' + tmp + 'c'
        elif i % 3 == 2:
            tmp = 'c' + tmp + 'a'
        else:
            tmp = 'b' + tmp + 'b'
        if tmp == s:
            ans = i
            break
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

    def test_入力例1(self):
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
