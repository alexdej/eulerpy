def problem6(n):
  return sum(i for i in xrange(1, n+1))**2 - sum(i**2 for i in xrange(1, n+1))

assert problem6(10) == 2640
print 'problem 6: %s' % problem6(100)

