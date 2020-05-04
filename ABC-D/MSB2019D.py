def resolve():
    n = int(input())
    s = input()
    d1 = [0] * 10
    d2 = [0] * 100
    d3 = [0] * 1000
    for i in s:
        seq = int(i)
        for j in range(100):
            if d2[j] == 1:
                d3[j * 10 + seq] = 1
        for k in range(10):
            if d1[k] == 1:
                d2[k * 10 + seq] = 1
        d1[seq] = 1
    print(sum(d3))


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
        input = """4
0224"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
123123"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19
3141592653589793238"""
        output = """329"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
