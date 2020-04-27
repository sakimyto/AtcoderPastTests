def resolve():
    sss = input()
    min_a = 0
    max_s = 0
    for i in range(len(sss)):
        if sss[i] == 'A':
            min_a = i
            break
    # for i in range(len(sss)-1, 0, -1):
    for i in reversed(range(len(sss))):
        if sss[i] == 'Z':
            max_s = i
            break
    print(max_s - min_a + 1)


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
        input = """QWERTYASDFZXCV"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ZABCZ"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """HASFJGHOGAKZZFEGA"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
