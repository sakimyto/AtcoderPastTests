def resolve():
    n, k = map(int, input().split())
    ppp = list(map(lambda x: int(x) - 1, input().split()))
    ccc = list(map(int, input().split()))
    ans = max(ccc)

    for i in range(n):
        tmp = 0
        score = [0]
        start = i
        while ppp[start] != i:
            start = ppp[start]
            tmp += ccc[start]
            score.append(tmp)
        loop_score = score[-1] + ccc[i]
        loop_len = len(score)

        for j in range(loop_len):
            if j <= k and j != 0:
                loops = (k - j) // loop_len
                thing = score[j] + max(0, loop_score) * loops
                ans = max(ans, thing)
            elif j == 0 and loop_len <= k:
                thing = loop_score * k // loop_len
                ans = max(ans, thing)
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
        input = """5 2
2 4 5 1 3
3 4 -10 -8 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 1
10 -7"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
3 1 2
-1000 -2000 -3000"""
        output = """-1000"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719"""
        output = """29507023469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
