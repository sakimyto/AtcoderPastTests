def resolve():
    n = int(input())
    aaa = list(map(int, input().split()))
    aaa.sort()
    judge = [1] * len(aaa)
    for i in range(len(aaa) - 1):
        if judge[i]:
            for j in range(i + 1, len(aaa)):
                if aaa[j] % aaa[i] == 0:
                    judge[j] = 0
            if aaa[i] == aaa[i + 1]:
                judge[i] = 0
        else:
            continue
    print(sum(judge))


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
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
