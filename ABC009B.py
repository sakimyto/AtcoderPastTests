def resolve():
    n = int(input())
    aaa = [int(input()) for _ in range(n)]
    aaa = sorted(set(aaa))
    print(aaa[-2])

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
        input = """4
100
200
300
300"""
        output = """200"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """5
50
370
819
433
120"""
        output = """433"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """6
100
100
100
200
200
200"""
        output = """100"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()