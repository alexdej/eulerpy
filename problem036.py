import util

digits = {
  '0': '000',
  '1': '001',
  '2': '010',
  '3': '011',
  '4': '100',
  '5': '101',
  '6': '110',
  '7': '111'
}

def bin(d):
  return ''.join(digits[c] for c in str(oct(d))[1:]).lstrip('0')

  
# brute force but only check odd numbers
def problem036(maximum):
  return sum(i for i in xrange(1, maximum, 2) if util.is_palindrome(str(i)) and util.is_palindrome(bin(i)))
  
    
    
print problem036(int(1e6))