def resolve():
    def divisors(n):
        lower_divisors, upper_divisors = [], []
        i = 1
        while i * i <= n:
            if n % i == 0:
                lower_divisors.append(i)
                if i != n // i:
                    upper_divisors.append(n // i)
            i += 1
        return lower_divisors + upper_divisors[::-1]

    n = int(input())
    print(*divisors(n), sep='\n')


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
        input = """6"""
        output = """1
2
3
6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """720"""
        output = """1
2
3
4
5
6
8
9
10
12
15
16
18
20
24
30
36
40
45
48
60
72
80
90
120
144
180
240
360
720"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000007"""
        output = """1
1000000007"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
