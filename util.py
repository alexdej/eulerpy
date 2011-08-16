# misc helpers

import itertools, math

def factorial(n):
  return product(i for i in xrange(1, n + 1))

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

def fibonacci_with_index():
  p1 = 1
  p2 = 1
  yield (1,p1)
  yield (2,p2)
  i = 2
  for n in itertools.count(1):
    q = p1 + p2
    p1 = p2
    p2 = q
    i = i + 1
    yield (i, q)

def n_choose_k(n, k):
  return factorial(n) / (factorial(k) * factorial(n-k))
    
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
  
def divisors(n):
  return [1] + sum(([d,n/d] for d in xrange(2, int(math.sqrt(n)) + 1) if not n % d), [])

