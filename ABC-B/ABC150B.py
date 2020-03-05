def resolve():
    # n = int(input())
    # s = input()
    # print(s.count('ABC'))
    #

    n = int(input())
    s = input()
    cnt = 0
    for i in range(n - 2):
        if s[i:i + 3] == 'ABC':
            cnt += 1
    print(cnt)

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
        input = """10
ZABCDBABCQ"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """19
THREEONEFOURONEFIVE"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """33
ABCCABCBABCCABACBCBBABCBCBCBCABCB"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
