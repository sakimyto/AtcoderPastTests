def resolve():
    n = int(input())
    s = input()
    w_cnt = [0] * (n + 2)
    e_cnt = [0] * (n + 2)
    for i in range(1, n + 1):
        if s[i - 1] == 'W':
            w_cnt[i] = 1 + w_cnt[i - 1]
        else:
            w_cnt[i] = w_cnt[i - 1]

    for i in range(1, n + 1):
        if s[-i] == 'E':
            e_cnt[n + 1 - i] = 1 + e_cnt[n + 2 - i]
        else:
            e_cnt[n + 1 - i] = e_cnt[n + 2 - i]
    ans = n
    for i in range(1, n + 1):
        tmp = w_cnt[i - 1] + e_cnt[i + 1]
        ans = min(ans, tmp)

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
        input = """5
WEEWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12
WEWEWEEEWWWE"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
WWWWWEEE"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
