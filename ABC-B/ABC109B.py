def resolve():
    n = int(input())
    www = [input() for _ in range(n)]
    ans = 'Yes'
    if len(list(set(www))) != n:
        ans = 'No'
    else:
        for i in range(1, n):
            if www[i][0] != www[i - 1][-1]:
                ans = 'No'
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
        input = """4
hoge
english
hoge
enigma"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
abc
arc
agc"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
