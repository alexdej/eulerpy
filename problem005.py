# http://projecteuler.net/index.php?section=problems&id=5
primes = [2, 3, 5, 7, 11, 13, 17, 19]

def invert(A):
  return [[a[i] for a in A] for i in xrange(0, len(A[0]))]

def smallest_divisible(n):
  p = largest_prime(n)
  i = p
  while True:
    if divisible(i, xrange(1, n + 1)):
	  return i
    i = i + p

def smallest_divisible_fast(n):
  fs = [factor(i) for i in xrange(2, n + 1)]
  fs = [max(f) for f in invert(fs)]
  return product([primes[i]**fs[i] for i in xrange(0, len(fs))])
  
def product(a):
  p = 1
  for n in a:
    p = p * n
  return p
  
def factor(n):
  f = []
  for i in xrange(0, len(primes)):
    f.append(0)
    while n % primes[i] == 0:
	  f[i] = f[i] + 1
	  n = n / primes[i]
  return f
	
def divisible(n, range):
  for i in range:
    if n % i != 0: 
	  return False
  return True
	
def largest_prime(n):
  return max(i if i < n else -1 for i in primes)
  
def test():
  assert largest_prime(10) == 7
  assert largest_prime(20) == 19
  assert not divisible(19, [2,3,4])
  assert divisible(12, [2,3,4])
  assert smallest_divisible(10) == 2520
  assert smallest_divisible_fast(10) == 2520
  assert factor(2520)[0] == 3
  print 'All tests pass.'

if __name__=="__main__":
  test()
  #print smallest_divisible(20)
  print smallest_divisible_fast(20)
  
  
  
