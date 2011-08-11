import math

# returns the n if is a triangle number, else 0
# t_n = 1/2(n)(n+1)
# n = abs(-.5 +/- sqrt(2*t_n + .25))
def get_triangle_number(t):
  return abs(math.sqrt(2 * t + .25) - .5)

def get_triangle_number_for_word(w):
  return get_triangle_number(sum(letter_to_number(c) for c in w))
  
def letter_to_number(c):
  return ord(c) - ord('A') + 1

def is_nonzero_integer(i):
  return i == int(i) and i > 0
  
def problem042(words):
  return [w for w in words if is_nonzero_integer(get_triangle_number_for_word(w))]
  
numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
assert all(get_triangle_number(numbers[i]) == i + 1 for i in xrange(0, len(numbers)))

f = open('data/problem042.txt')
words = f.read().replace('"','').split(',')
f.close()

print len(problem042(words))

#print [(w, get_triangle_number_for_word(w)) for w in words]