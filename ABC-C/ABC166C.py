def resolve():
    n, m = map(int, input().split())
    hhh = list(map(int, input().split()))
    aabb = [list(map(int, input().split())) for _ in range(m)]
    cnt = [0] * n
    for i in range(m):
        if hhh[aabb[i][0] - 1] == hhh[aabb[i][1] - 1]:
            cnt[aabb[i][0] - 1] = -1
            cnt[aabb[i][1] - 1] = -1
        elif hhh[aabb[i][0] - 1] > hhh[aabb[i][1] - 1]:
            if cnt[aabb[i][0] - 1] >= 0:
                cnt[aabb[i][0] - 1] = 1
            cnt[aabb[i][1] - 1] = -1
        else:
            if cnt[aabb[i][1] - 1] >= 0:
                cnt[aabb[i][1] - 1] = 1
            cnt[aabb[i][0] - 1] = -1
    print(cnt.count(0) + cnt.count(1))


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
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
