# helper functions dealing with prime numbers and factorization

import itertools, math

# erat2 from http://onlamp.com/pub/a/python/excerpt/pythonckbk_chap1/index1.html?page=2
def erat2( ):
    D = {  }
    yield 2
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p is None:
            D[q*q] = q
            yield q
        else:
            x = p + q
            while x in D or not (x&1):
                x += p
            D[x] = p

def factors(n, ps=None):
  fs = []
  if not ps:
    ps = erat2()
  for p in ps:
    if p > n:
      break
    while not n % p:
      fs.append(p)
      n = n / p
  return fs

def is_prime(n):
  m = math.sqrt(n)
  for p in erat2():
    if p > m:
      break
    elif n % p == 0:
      return False
  return True

def primes(maximum):
  return itertools.takewhile(lambda x: x <= maximum, erat2())