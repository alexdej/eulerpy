import util

def problem021(n):
  return sum(i for i in xrange(1, n) if amicable_pair(i))
  
def amicable_pair(a):
  b = sum(util.divisors(a))
  return (a, b) if a != b and sum(util.divisors(b)) == a else None

def test():  
  assert amicable_pair(220)[1] == 284
  assert amicable_pair(284)[1] == 220


def solution():
  print problem021(10000)