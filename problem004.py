import util
def problem4(m):
  return max(n for n in (a * b for a in xrange(m, -1, -1) for b in xrange(m, -1, -1)) if util.is_palindrome(str(n)))

assert problem4(99) == 9009
print 'problem 4: %s' % problem4(999)
  
