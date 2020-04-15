def resolve():
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b + 1):
        i = str(i)
        if i == i[::-1]:
            ans += 1
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
        input = """11009 11332"""
        output = """4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """31415 92653"""
        output = """612"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()