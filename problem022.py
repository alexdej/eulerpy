def problem022(names):
  return sum((i+1)*score(names[i]) for i in xrange(0, len(names)))
      
def score(name):
  return sum(value(c) for c in name)

def value(l):
  return ord(l) - ord('A') + 1
  
if __name__=="__main__":
  f = open('data/problem022.txt')
  names = f.read().replace('"','').split(',')
  f.close()
  names.sort()
  
  print 'read %d names' % len(names)
  assert (names.index('COLIN')+1)*score('COLIN')==49714 
  assert score('COLIN') == 53
  
  print problem022(names)