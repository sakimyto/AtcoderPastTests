def resolve():
    from collections import Counter
    s = input()[::-1]
    cnt = [0]
    d = 0
    mod = 2019

    for i in s:
        tmp = int(i) * pow(10, d, mod) % mod
        tmp = cnt[-1] + tmp
        cnt.append(tmp % mod)
        d += 1

    cnt = Counter(cnt)
    ans = sum(j * (j - 1) // 2 for j in cnt.values())
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
        input = """1817181712114"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """14282668646"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2119"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
