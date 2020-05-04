def resolve():
    sa = list(input())
    sb = list(input())
    sc = list(input())
    tmp = 'a'
    for i in range(10000):
        if tmp == 'a':
            if len(sa) == 0:
                print('A')
                break
            tmp = sa[0]
            del sa[0]
        elif tmp == 'b':
            if len(sb) == 0:
                print('B')
                break
            tmp = sb[0]
            del sb[0]
        else:
            if len(sc) == 0:
                print('C')
                break
            tmp = sc[0]
            del sc[0]


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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
