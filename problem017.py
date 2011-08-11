ones = ['one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
def num_to_text(n):
  assert n < int(1e6) # doesn't handle millions
  s = ''
  while n > 0:
    if n >= 1000:
      s = s + num_to_text(n / 1000) + ' thousand '
      n = n - ((n / 1000) * 1000)
    elif n >= 100:
      s = s + num_to_text(n / 100) + ' hundred '
      n = n - ((n / 100) * 100)
    elif n >= 20:    
      if len(s) > 0:
        s = s + 'and '
      s = s + tens[n / 10 - 2] + ' '
      n = n - ((n / 10) * 10)
    else:
      if len(s) > 0 and s[-2] != 'y': # total hack :)
        s = s + 'and '
      s = s + ones[n - 1]
      n = n - n
  return s.strip()
      
def problem017(n):
  return sum(len(num_to_text(i).replace(' ','')) for i in xrange(1, n + 1))

assert num_to_text(1000) == 'one thousand'
assert num_to_text(45) == 'forty five'
assert num_to_text(340) == 'three hundred and forty'

assert problem017(5) == 19
print problem017(1000)

#for i in xrange(1, 101):
  #print num_to_text(i)