import util, primes

def problem7(n):
  return util.nth(n, primes.erat2())
print 'problem 7: %s' % problem7(1e4)

