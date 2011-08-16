# originally solved this with pen & paper but decided to go back and do a code solution for fun

# inputs is the list of correct inputs as strings
def problem079(inputs):
  # construct a graph of all inputs
  g = {}
  for s in inputs:
    for i in xrange(0,len(s)):
      c = s[i]
      if not c in g:
        g[c] = set()
      if i+1 < len(s):
        g[c].add(s[i+1])

  # do a topological sort of g
  discovered = {}
  sorted = []
  for x in g:
    if not x in discovered:
      dfs(g, x, discovered, sorted)
  sorted.reverse()
  return sorted
        
def dfs(g, x, discovered, sorted):
  discovered[x] = True
  for y in g[x]:
    if not y in discovered:
      dfs(g, y, discovered, sorted)
  sorted.append(x)
  
f = open('data/problem079.txt')
inputs = f.read().splitlines()
f.close()
print ''.join(problem079(inputs))