def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    right = 0
    tmp = [0] * (10 ** 5 + 1)
    cnt = 0
    ans = 0
    for left in range(n):
        while right < n and tmp[aaa[right]] == 0:
            tmp[aaa[right]] = 1
            cnt += 1
            right += 1
        ans = max(ans, cnt)
        if left == right:
            right += 1
        else:
            tmp[aaa[left]] -= 1
            cnt -= 1
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

    def test_入力例1(self):
        input = """7
1 2 1 3 1 4 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """1
100"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
