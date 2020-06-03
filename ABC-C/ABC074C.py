def resolve():
    A, B, C, D, E, F = list(map(int, input().split()))

    # A+B のアリエル値
    a_plus_b = set()
    for i in range(0, 31, A):
        for j in range(0, 31, B):
            if not (i == 0 and j == 0):
                if i + j <= 30:
                    a_plus_b.add(i + j)

    c_plus_d = set()
    for i in range(0, F, C):
        for j in range(0, F, D):
            if i + j <= F:
                c_plus_d.add(i + j)

    max_concent = -1
    ans_sum = 0
    ans_sugar = 0
    # print(c_plus_d)
    # print(a_plus_b)
    for cd in c_plus_d:
        for ab in a_plus_b:
            if cd <= E * ab and cd <= F - 100 * ab:
                if max_concent <= cd / ab:
                    max_concent = cd / ab
                    ans_sum = 100 * ab + cd
                    ans_sugar = cd

    print(str(ans_sum) + " " + str(ans_sugar))




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
        input = """3
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
