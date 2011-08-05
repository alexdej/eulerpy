import util
def problem9(n):
  return util.product(util.nth(1, ((a,b,c) for a in xrange(1, n) for b in xrange(1, n) for c in xrange(1, n) if a+b+c == n and a**2 + b**2 == c**2)))
print 'problem 9: %s' % problem9(1000)
  
