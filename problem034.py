import util

factorials = [util.factorial(i) for i in xrange(0, 10)]
def problem034():
  return sum(i for i in xrange(3, factorials[9]*7) if i == sum_of_digit_factorial(i))

def sum_of_digit_factorial(n):
  return sum(factorials[int(c)] for c in str(n))
  
def solution():
  return problem034()

def test():
  assert sum_of_digit_factorial(145) == 145
  
test()
print solution()