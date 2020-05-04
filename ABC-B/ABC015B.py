def resolve():
    import math
    n = int(input())
    aaa = list(map(int, input().split()))
    cnt = 0
    num = 0
    for a in aaa:
        if a != 0:
            cnt += a
            num += 1
    print(math.ceil(cnt / num))


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
        input = """4
0 1 3 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
1 4 9 10 15"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
