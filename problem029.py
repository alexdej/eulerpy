def problem029(n):
  return len(set(
    a**b for a in xrange(2, n + 1) for b in xrange(2, n + 1)))
    
assert problem029(5) == 15
print problem029(100)