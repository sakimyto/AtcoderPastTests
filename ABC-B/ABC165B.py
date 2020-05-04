def resolve():
    import math
    x = int(input())
    cnt = 100
    ans = 0
    for _ in range(10 ** 7):
        cnt = math.floor(cnt * 1.01)
        ans += 1
        if cnt >= x:
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

    def test_入力例_1(self):
        input = """103"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
