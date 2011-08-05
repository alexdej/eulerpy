import itertools
import util

def problem2(m):
  return sum(n for n in itertools.takewhile(lambda x: x < m, util.fibonacci()) if not n % 2)
print 'problem 2: %s' % problem2(4e6)

