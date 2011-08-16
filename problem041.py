import primes, itertools

#slow way: search primes for pandigital numbers
def problem041(n):
  return max(
    itertools.ifilter(is_pandigital, 
        itertools.takewhile(lambda x: x < n, 
            primes.erat2())))

def is_pandigital(x):
  s = list(str(x))
  s.sort()
  for i in xrange(0, len(s)):
    if s[i] != chr(ord('1') + i):
      return False
  return True
  
assert is_pandigital(2143)
assert not is_pandigital(2243)

# faster way: generate pandigital numbers and check for prime
# start from 7 because every 8- and 9-digit pandigital number is divisible by 3
# using sum-of-digits trick: 8+7+6+5+4+3+2+1 == 36, 9+8+7+6+5+4+3+2+1 == 45
def problem041_fast(n):
  for i in xrange(7, 0, -1):
    for pd in pandigitals(i):
      if isprime(pd):
        return pd
  return None

digits = '987654321'
def pandigitals(n):
  s = ''.join(digits[i] for i in xrange(len(digits) - n, len(digits)))
  for p in permute(s):
    yield int(p)

def isprime(x):
  return x & 1 and len(primes.factors(x)) == 0
  
def permute(s):
  if len(s) == 0:
    yield ''
  else:
    for i in xrange(0, len(s)):
      for p in permute(s[0:i] + s[i+1:]):
        yield s[i] + p
      
assert list(permute('012')) == ['012','021','102','120','201','210']
assert list(pandigitals(3)) == [321, 312, 231, 213, 132, 123]
#print problem041(1e10)
print problem041_fast(1e10)