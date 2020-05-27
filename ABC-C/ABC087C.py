def resolve():
    import itertools
    n = int(input())
    aa1 = list(map(int, input().split()))
    aa2 = list(map(int, input().split()))
    aa2.reverse()
    aa1 = list(itertools.accumulate(aa1))
    aa2 = list(itertools.accumulate(aa2))
    aa2.reverse()
    ans = 0
    for i in range(n):
        tmp = aa1[i] + aa2[i]
        ans = max(ans, tmp)
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
3 2 2 4 1
1 2 2 2 1"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
3 3 4 5 4 5 3
5 3 4 4 2 3 2"""
        output = """29"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
2
3"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
