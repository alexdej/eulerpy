import itertools
def problem030(p):
  return sum(matches(p))

def matches(p):
  return (n for n in xrange(10, maximum(p) + 1) if n == sum(d**p for d in digits(n)))
  
def digits(n):
  return [int(d) for d in str(n)]

# computes the highest possible value for we need to consider for a given power p
def maximum(p):
  for i in itertools.count(1):
    if len(str(i*9**p)) < i:
      return (i-1)*9**p

#print [maximum(n) for n in xrange(1, 10)]
assert problem030(4)==19316
#print list(matches(5))
print problem030(5)

