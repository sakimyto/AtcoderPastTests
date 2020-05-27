def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    max_a = max(aaa)
    cnt = [0] * (max_a + 3)
    cnt_sum = [0] * (max_a + 2)
    for a in aaa:
        if a == 0:
            cnt[a] += 1
            cnt[a + 2] -= 1
        else:
            cnt[a - 1] += 1
            cnt[a + 2] -= 1
    cnt_sum[0] = cnt[0]
    for i in range(1, max_a + 2):
        cnt_sum[i] = cnt_sum[i - 1] + cnt[i]
    print(max(cnt_sum))


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
        input = """7
3 1 4 1 5 9 2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
0 1 2 3 4 5 6 7 8 9"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
99999"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
