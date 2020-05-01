def resolve():
    s = input()
    t = input()
    lis_r = list('atcoder')
    ans = 'You can win'
    for s, t in zip(s, t):
        if (s == t) or (s == '@' and t in lis_r) or (t == '@' and s in lis_r):
            continue
        else:
            ans = 'You will lose'
            break
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

    def test_入力例_1(self):
        input = """ch@ku@ai
choku@@i"""
        output = """You can win"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aoki
@ok@"""
        output = """You will lose"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """arc
abc"""
        output = """You will lose"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
