def resolve():
    s = input()
    tmp = s[0]
    cnt = 0
    ans = []
    for i in range(len(s)):
        if tmp != s[i]:
            ans.append(tmp)
            ans.append(str(cnt))
            tmp = s[i]
            cnt = 1
        else:
            cnt += 1

    ans.append(tmp)
    ans.append(str(cnt))

    print(''.join(ans))


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
        input = """aabbbaad"""
        output = """a2b3a2d1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aabbbbbbbbbbbbxyza"""
        output = """a2b12x1y1z1a1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """edcba"""
        output = """e1d1c1b1a1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
