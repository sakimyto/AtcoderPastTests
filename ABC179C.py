def resolve():
    # n = int(input())
    # cnt = 0
    # for a in range(1, n):
    #     for b in range(1, n):
    #         if a * b < n:
    #             cnt += 1
    #         else:
    #             break
    # print(cnt)

    n = int(input())
    ans = 0
    for a in range(1, n):
        ans += (n - 1) // a
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
        input = """3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100"""
        output = """473"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000"""
        output = """13969985"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
