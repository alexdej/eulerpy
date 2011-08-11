def problem016(n):
  return sum(int(c) for c in str(2**n))
  
assert problem016(15) == 26
print problem016(1000)