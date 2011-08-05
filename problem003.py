import primes

def problem3(n):
  return max(primes.factors(n))

assert problem3(13195) == 29
print 'problem 3: %s' % problem3(600851475143)
  
