def resolve():
    w = input()
    ans = ''
    for i in w:
        if i not in 'aiueo':
            ans += i
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
        input = """chokudai"""
        output = """chkd"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """okanemochi"""
        output = """knmch"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """aoki"""
        output = """k"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """mazushii"""
        output = """mzsh"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
