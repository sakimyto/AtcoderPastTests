def resolve():
    n = int(input())
    ans = 'No'
    for i in range(100):
        for j in range(100):
            if 4 * i + 7 * j == n:
                ans = 'Yes'
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
        input = """11"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
