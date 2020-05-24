def resolve():
    k = int(input())
    s = input()
    if len(s) > k:
        print(s[0:k] + '...')
    else:
        print(s)


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
        input = """7
nikoandsolstice"""
        output = """nikoand..."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40
ferelibenterhominesidquodvoluntcredunt"""
        output = """ferelibenterhominesidquodvoluntcredunt"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
