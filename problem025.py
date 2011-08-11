import util
import itertools

def problem025(digits):
  return itertools.dropwhile(lambda x: len(str(x[1])) < digits, util.fibonacci_with_index()).next()
  
print problem025(10)
print problem025(100)
print problem025(1000)