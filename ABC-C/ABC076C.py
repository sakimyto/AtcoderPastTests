def resolve():
    s = input()
    t = input()

    def match(k):
        flag = True
        for i in range(len(t)):
            if s[i + k] != t[i] and s[i + k] != "?":
                flag = False
                break
        return flag

    flag = False
    # reversed するのはなぜ
    for k in reversed(range(len(s) - len(t) + 1)):
        if match(k):
            s = s[:k] + t + s[k + len(t):]
            flag = True
            break

    if flag:
        print(s.replace('?', 'a'))
    else:
        print('UNRESTORABLE')


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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """?
c"""
        output = """c"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
