# http://www.yodle.com/careers/job-details/senior-software-engineer-new-york-ny/
def solve(data):
  # working upwards from the bottom of the triangle (actually the second row
  # from the bottom), compute the maximum sum from that position and store it 
  # in place
  for i in xrange(len(data) - 2, -1, -1):
    assert len(data[i]) == i + 1
    for j in xrange(0, len(data[i])):
	  data[i][j] = data[i][j] + max(data[i+1][j], data[i+1][j+1])

  return data[0][0] if len(data) > 0 else 0

def test():
  assert solve([[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]]) == 27
  assert solve([[65], [76, 4], [69, 1, 6], [88, 2, 9, 1]]) == 298
  assert solve([[65], [2, 76], [3, 1, 69], [11, 2, 9, 88]]) == 298
  assert solve([[5]]) == 5
  assert solve([]) == 0

if __name__=="__main__":
  test()
  
  f = open('problem018_triangle.txt')
  print solve([[int(s) for s in l.split()] for l in f.readlines()])
  f.close()