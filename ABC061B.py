def resolve():
    n, m = map(int, input().split())
    cnt = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        cnt[a - 1] += 1
        cnt[b - 1] += 1
    print(*cnt, sep='\n')


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
        input = """4 3
1 2
2 3
1 4"""
        output = """2
2
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5
1 2
2 1
1 2
2 1
1 2"""
        output = """5
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8"""
        output = """3
3
2
2
2
1
1
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
