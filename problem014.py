cache = [0] * int(1e6)
def problem014():
  #return max((n for n in xrange(1, int(1e6))), key=lambda x: len(sequence(x)))
  return max((n for n in xrange(1, int(1e6))), key=lambda x: seq_len(x))

def seq_len(n):
  if n == 1:
    return 1
  elif n < len(cache):
    if cache[n] == 0:
      cache[n] = 1 + seq_len(3 * n + 1 if n & 1 else n / 2)
    return cache[n]
  else:
    return 1 + seq_len(3 * n + 1 if n & 1 else n / 2)
  
def sequence(n):
  if n % int(1e5) == 0:
    print n
  seq = []
  while n > 1:
    seq.append(n)
    if n & 1 == 0: #even
      n = n / 2
    else: #odd
      n = 3 * n + 1
  return seq + [n]

assert len(sequence(13)) == 10
assert seq_len(13) == 10
print problem014()