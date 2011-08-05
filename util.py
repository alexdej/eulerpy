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

def nth(n, iterable):
  return itertools.islice(iterable, n, None).next()