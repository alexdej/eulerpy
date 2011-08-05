# misc helpers

import itertools

def fibonacci():
  yield 1
  yield 2
  p1 = 1
  p2 = 2
  for n in itertools.count(1):
    q = p1 + p2
    p1 = p2
    p2 = q
    yield q
    
def product(A):
  p = 1
  for a in A:
    p = p * a
  return p
  
def readfile(filename):
  f = open(filename)
  s = f.read()
  f.close()
  return s
  
def is_palindrome(s):
  return s == s[::-1]

def nth(n, iterable):
  return itertools.islice(iterable, n, None).next()