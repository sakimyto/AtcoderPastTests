def resolve():
    x = input()
    ans = 'YES'
    for choku in ['ch', 'o', 'k', 'u']:
        x = x.replace(choku, '')
    if x != '':
        ans = 'NO'
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
        input = """chokuou"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """kuccho"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """atcoder"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
