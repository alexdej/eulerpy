# english language frequencies
english = {'e':.127, 't':.091, 'a':.082, 'o':.075, 'i':.070, 's':.063}
def decipher(cipher, key):
  plain = [cipher[i] ^ key[i % len(key)] for i in xrange(0, len(cipher))]
  return ''.join(map(chr, plain))

def englishness(text):
  fs = frequencies(text)
  return sum(abs(fs.get(k,0.0) - english[k]) / english[k] for k in english.keys())

def frequencies(text):
  counts = {}
  for c in text:
    counts[c] = counts.get(c,0) + 1
  return dict((k, float(v) / len(text)) for k, v in counts.items())

def frequency(text, letter):
  return float(sum(1 if c == letter else 0 for c in text)) / len(text)
  
def test():
  assert len(all_keys()) == 26 * 26 * 26
  print 'All tests pass'

alpha = map(chr, range(97,123))
def all_keys():
  return [a + b + c for a in alpha for b in alpha for c in alpha]
def all_keys2():
  return ['g' + b + c for b in alpha for c in alpha]
  
if __name__=="__main__":
  
  test()

  f = open('data/problem059.txt')
  cipher = map(int, f.read().split(','))
  f.close()
  
  #print englishness(decipher(cipher, map(ord, 'god')))
  
  candidates = []
  for key in all_keys():
    s = decipher(cipher, map(ord, key))
    e = englishness(s)
    if e < 2.0:
	  candidates.append((key, e, s))
  
  for candidate in candidates:
    print '%s (%s): %s' % candidate
    print sum(map(ord, candidate[2]))

  
  print 'done'
  #print all_keys()
