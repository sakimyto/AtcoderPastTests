def resolve():
    h, w = map(int, input().split())

    def defs(h, w):
        ans = 10 ** 12
        for i in range(1, h):
            sa = i * w
            h2 = h - i

            for j in range(2):
                if j == 0:
                    sb = h2 * (w // 2)
                    sc = h2 * (w - (w // 2))
                else:
                    sb = (h2 // 2) * w
                    sc = (h - i - (h2 // 2)) * w

                s_max = max(sa, sb, sc)
                s_min = min(sa, sb, sc)

                ans = min(ans, s_max - s_min)
        return ans

    print(min(defs(h, w), defs(w, h)))


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
        input = """3 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """100000 100000"""
        output = """50000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
