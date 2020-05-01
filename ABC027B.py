def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    cnt = 0
    if sum(aaa) % n != 0:
        cnt = -1
    else:
        avg = sum(aaa) / n
        for i in range(1, n):
            if sum(aaa[:i]) != i * avg:
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

    def test_入力例1(self):
        input = """3
1 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5
2 0 0 0 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """2
0 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4
0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
