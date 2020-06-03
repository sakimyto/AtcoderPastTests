def resolve():
    s = input()
    kb = 'WBWBWWBWBWBW' * 10
    scale = ['Do', 'Do', 'Re', 'Re', 'Mi', 'Fa', 'Fa', 'So', 'So', 'La', 'La', 'Si']
    for i in range(20):
        if s == kb[i:i + 20]:
            print(scale[i])
            break


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
        input = """WBWBWWBWBWBWWBWBWWBW"""
        output = """Do"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """WWBWBWBWWBWBWWBWBWBW"""
        output = """Mi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
