def problem048():
  return sum(i ** i for i in xrange(1, 1001))

  
print problem048()
print str(problem048())[-10:]