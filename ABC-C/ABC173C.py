def resolve():
    h, w, k = map(int, input().split())
    ccc = [input() for _ in range(h)]
    ans = 0
    for bit_h in range(2 ** h):
        for bit_w in range(2 ** w):
            cnt = 0
            for hi in range(h):
                for wi in range(w):
                    if (bit_h >> hi) & 1 == 0 and (bit_w >> wi) & 1 == 0:
                        if ccc[hi][wi] == '#':
                            cnt += 1
            if cnt == k:
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
        input = """2 3 2
..#
###"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 4
..#
###"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 3
##
##"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 6 8
..##..
.#..#.
#....#
######
#....#
#....#"""
        output = """208"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
