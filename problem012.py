import itertools, primes, util

# What is the value of the first triangle number to have over five hundred (n) divisors?
def problem012(n):
  #g = triangle_numbers()
  g = itertools.count(1)
  #if n > 100:
  #  g = itertools.dropwhile(lambda x: x < 1e7, g)
  return triangle_number(itertools.dropwhile(lambda x: triangle_divisors(x) < n, g).next())
  
def triangle_numbers():
  n = 0
  for i in itertools.count(1):
    n = n + i
    yield n
    
# where n is the 'nth' triangle number eg 1==1,2==3,3==6,etc
p = list(primes.primes(10000))
def triangle_divisors(n):
  return divisors(n if n & 1 else n / 2) * divisors(n+1 if not n & 1 else (n+1)/2)

def divisors(n):
  factors = {}
  for f in primes.factors(n, p):
    if not f in factors:
      factors[f] = 1
    factors[f] = factors[f] + 1
  return util.product(factors.values())
  
def triangle_number(n):
  return n * (n+1) / 2

def test(): 
  assert problem012(5) == 28

def solution():
  return problem012(500)
print solution()