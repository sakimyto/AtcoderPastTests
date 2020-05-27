def resolve():
    s = input()
    words = []
    tmp = ''
    for c in s:
        tmp += c
        if c.isupper() and len(tmp) >= 2:
            words.append(tmp)
            tmp = ''

    print(''.join(sorted(words, key=str.lower)))


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
        input = """FisHDoGCaTAAAaAAbCAC"""
        output = """AAAaAAbCACCaTDoGFisH"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AAAAAjhfgaBCsahdfakGZsZGdEAA"""
        output = """AAAAAAAjhfgaBCsahdfakGGdEZsZ"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
