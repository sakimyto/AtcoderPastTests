def resolve():
    s = input()
    while len(s) > 4:
        if s[-5:] == 'dream' or s[-5:] == 'erase':
            s = s[:-5]
            continue
        elif s[-7:] == 'dreamer':
            s = s[:-7]
            continue
        elif s[-6:] == 'eraser':
            s = s[:-6]
            continue
        else:
            break
    if len(s) > 0:
        print('NO')
    else:
        print('YES')



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
        input = """erasedream"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """dreameraser"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """dreamerer"""
        output = """NO"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
