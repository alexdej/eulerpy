def problem1(m):
  return sum(n for n in xrange(1, m) if not n % 5 or not n % 3)

assert problem1(10) == 23
print 'problem 1: %s' % problem1(1000)
