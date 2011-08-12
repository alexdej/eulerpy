from util import factorial

# number of paths through an mxn grid without backtracking
# defined by i-choose-k where i:m+n and k:n
def problem015(m, n):
  return factorial(m + n) / (factorial(m) * factorial(n))
  
assert problem015(2,2) == 6
print problem015(20,20)