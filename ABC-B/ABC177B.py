def resolve():
    s = input()
    t = input()
    len_s = len(s)
    len_t = len(t)
    ans = len_t
    for i in range(len_s - len_t + 1):
        tmp_cnt = 0
        tmp_s = s[i:i + len_t]
        for c1, c2 in zip(tmp_s, t):
            if c1 != c2:
                tmp_cnt += 1
        ans = min(ans, tmp_cnt)
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
        input = """cabacc
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """codeforces
atcoder"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
