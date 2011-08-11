import util
def problem020(n):
  return sum(int(c) for c in str(util.factorial(n)))
  
assert problem020(10) == 27
print problem020(100)