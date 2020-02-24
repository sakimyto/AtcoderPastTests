def resolve():
    from itertools import permutations
    n, m = map(int, input().split())
    ab = [[] for i in range(n)]
    for i in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        ab[a].append(b)
        ab[b].append(a)
    cnt = 0
    if n == 2:
        if 1 in ab[0]:
            print(1)
        else:
            print(0)
        exit()
    for p in permutations(range(1, n)):
        if p[0] in ab[0]:
            flag = True
            for i in range(n - 2):
                if p[i + 1] not in ab[p[i]]:
                    flag = False
                    break
            if flag:
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

    def test_入力例_1(self):
        input = """3 3
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
