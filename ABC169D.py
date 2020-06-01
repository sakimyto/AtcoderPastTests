def resolve():
    import itertools

    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])

        if temp != 1:
            arr.append([temp, 1])

        if arr == []:
            arr.append([n, 1])

        return arr

    n = int(input())
    n_list = factorization(n)
    cnt = 0
    cnt_list = range(100)
    cnt_list = list(itertools.accumulate(cnt_list))
    for i in n_list:
        tmp = 0
        if i[0] != 1:
            for j in range(1, 100):
                if cnt_list[j] <= i[1]:
                    tmp = j
                else:
                    cnt += tmp
                    break
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
        input = """24"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """64"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1000000007"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """997764507000"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
