import itertools

def problem028(n):
  return sum(itertools.chain(
    sequence(3, 10, 8, n**2),
    sequence(5, 12, 8, n**2),
    sequence(7, 14, 8, n**2),
    sequence(9, 16, 8, n**2))) + 1


def sequence(start, first_incr, incr_incr, n):
  i = start
  incr = first_incr
  while i <= n:
    yield i
    i = i + incr
    incr = incr + incr_incr

assert problem028(5) == 101
print problem028(1001)