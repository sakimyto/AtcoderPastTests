def resolve():
    a, b, x = map(int, input().split())

    def is_ok(arg):
        return a * arg + b * len(str(arg)) <= x

    def meguru_bisect(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    print(meguru_bisect(10 ** 9 + 1, 0))



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
        input = """10 7 100"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 100000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1234 56789 314159265"""
        output = """254309"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
