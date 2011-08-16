import util

def problem024():
  return util.nth(int(1e6) - 1, permute('0123456789'))
  
def permute(s):
  if len(s) == 0:
    yield ''
  else:
    for i in xrange(0, len(s)):
      for p in permute(s[0:i] + s[i+1:]):
        yield s[i] + p
      
assert list(permute('012')) == ['012','021','102','120','201','210']

print problem024()