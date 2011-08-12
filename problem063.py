import itertools

# find numbers i^n where len(str(i^n))==n
# i will be <10 since len(str(10^n))>n for all n
def problem063():
  ans = []
  for i in itertools.count(1):
    any = False
    for n in powers(i):
      if len(str(n)) == i:
        ans.append(n)
        any = True
      elif len(str(n)) > i:
        break
    if not any: 
      break
  return ans
  
def powers(n):
  for x in xrange(1, 11):
    yield x ** n
    
print problem063()
print len(problem063())