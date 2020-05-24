def resolve():
    n = int(input())

    def primes(n):
        p_list = [2]
        for i in range(2, n + 1):
            for p in p_list:
                if i % p == 0:
                    break
            else:
                p_list.append(i)

        return p_list

    p_list = primes(n)
    xxx = [1] * len(p_list)

    for j in range(1, n + 1):
        tmp = j
        num = 0

        while tmp > 1:
            if tmp % p_list[num] == 0:
                tmp = tmp / p_list[num]
                xxx[num] += 1
            else:
                num += 1

    cnt = 1
    for x in xxx:
        cnt = (cnt * x) % (1e9 + 7)

    print(int(cnt))



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
        input = """3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000"""
        output = """972926972"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
