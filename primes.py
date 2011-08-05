# helper functions dealing with prime numbers and factorization

import itertools

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

def factors(n):
  fs = []
  for p in erat2():
    if p > n:
      break
    elif n % p == 0:
      fs.append(p)
      while n % p == 0:
        n = n / p
  return fs

