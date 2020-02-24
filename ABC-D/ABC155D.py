def resolve():
    # import itertools
    # import heapq
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # multi_list = []
    # for x, y in itertools.combinations(a, 2):
    #     multi_list.append(x * y)
    # heapq.heapify(multi_list)
    # for _ in range(k - 1):
    #     heapq.heappop(multi_list)
    # print(heapq.heappop(multi_list))

    import numpy as np
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a = np.array(a)
    a.sort()
    zero_cnt = np.count_nonzero(a == 0)
    plus = a[a > 0]
    minus = a[a < 0]

    def count(x):  # 積がx以下になるペアの個数を返す
        ans = 0
        if x >= 0:
            ans += n * zero
        ans += np.searchsorted(a, x // plus, side="right").sum()
        ans += n * len(minus) - np.searchsorted(a, -(-x // minus), side="left").sum()
        ans -= np.count_nonzero(a * a <= x)  # 同じものはふたつ選べない
        return ans // 2

    ok = 10 ** 18
    ng = -ok - 1
    while ok - ng > 1:
        cur = (ok + ng) // 2
        if count(cur) >= K:
            ok = cur
        else:
            ng = cur
    print(int(ok))


import time

if __name__ == '__main__':
    start = time.time()
    for i in range(0, 11):
        print("a")
    elapsed_time = time.time() - start
    print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

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
3 3 -4 -2"""
        output = """-6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40
5 4 3 2 -1 0 0 0 0 0"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 413
-170202098 -268409015 537203564 983211703 21608710 -443999067 -937727165 -97596546 -372334013 398994917 -972141167 798607104 -949068442 -959948616 37909651 0 886627544 -20098238 0 -948955241 0 -214720580 277222296 -18897162 834475626 0 -425610555 110117526 663621752 0"""
        output = """448283280358331064"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
