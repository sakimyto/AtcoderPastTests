def resolve():
    s = input()
    alps = 'abcdefghijklmnopqrstuvwxyz'
    for alp in alps:
        if alp not in s:
            print(alp)
            break
    else:
        print('None')


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
        input = """atcoderregularcontest"""
        output = """b"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """None"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg"""
        output = """d"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()