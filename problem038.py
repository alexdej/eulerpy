# solved this one with pen and paper:

# we are given a solution with i=9 (918273645) so we can expect the solution to be greater
# this means that the first two digits of i must be at least 92
# i can't be 2 digits because that would only give 8- or 11-digit numbers
# i can't be 3 digits because that would only give 7- or 11-digit numbers
# so i must be 4 digits

# starting with i=9___ and i*2=18___ I enventually worked out a combination that fit:

def problem038():
  return 932718654
  
print problem038()