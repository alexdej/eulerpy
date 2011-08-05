# from http://norvig.com/sudoku.html

def cross(A, B):
  return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + 
            [cross(r, cols) for r in rows] +
			[cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def solve(grid):
  return search(parse_grid(grid))
  
def search(values):
  if values is False:
    return False
  if all(len(values[s]) == 1 for s in squares):
    return values
  n,s = min((len(values[s]), s) for s in squares if len(values[s]) > 1)
  return some(search(assign(values.copy(), s, d)) for d in values[s])
  
def some(seq):
  for e in seq:
    if e: return e
  return False

def parse_grid(grid):
  values = dict((s, digits) for s in squares)
  for s,d in grid_values(grid).items():
    if d in digits and not assign(values, s, d):
	  return False 
  return values
  
def grid_values(grid):
  chars = [c for c in grid if c in digits or c in '0.']
  assert len(chars) == 81
  return dict(zip(squares, chars))
  
def assign(values, s, d):
  other_values = values[s].replace(d, '')
  if all(eliminate(values, s, d2) for d2 in other_values):
    return values
  else:
    return False

def eliminate(values, s, d):
  if d not in values[s]:
    return values
  values[s] = values[s].replace(d, '')
  if len(values[s]) == 0:
    return False
  elif len(values[s]) == 1:
    d2 = values[s]
    if not all(eliminate(values, s2, d2) for s2 in peers[s]):
      return False
  for u in units[s]:
    dplaces = [s for s in u if d in values[s]]
    if len(dplaces) == 0:
      return False
    elif len(dplaces) == 1:
      if not assign(values, dplaces[0], d):
        return False
  return values
  
def display(values):
  width = 1+max(len(values[s]) for s in squares)
  line = '+'.join(['-'*(width*3)]*3)
  for r in rows:
    print ''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols)
    if r in 'CF': print line
  print
    
def test():
  assert len(squares) == 81
  assert len(unitlist) == 27
  assert all(len(units[s]) == 3 for s in squares)
  assert all(len(peers[s]) == 20 for s in squares)
  assert units['C2'] == [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
						 ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
						 ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
  assert peers['C2'] == set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2', 
                             'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
							 'A1', 'A3', 'B1', 'B3'])
  
  test_solve('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..',
             '483921657967345821251876493548132976729564138136798245372689514814253769695417382')
  test_solve('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......', 
             '417369825632158947958724316825437169791586432346912758289643571573291684164875293')
  # this one takes a long time
  #test_solve('.....6....59.....82....8....45........3........6..3.54...325..6..................', 
  #           '438796215659132478271458693845219367713564829926873154194325786362987541587641932')
  print 'All tests pass.'

def test_solve(grid, solution):
  values = solve(grid)
  assert all(len(values[s]) == 1 for s in squares)
  assert ''.join(values[s] for s in squares) == solution
  
if __name__ == '__main__':
  test()
  
  f = open('problem096_sudoku.txt')
  grids = []
  grid = ''
  for l in f.readlines():
    if l.startswith('Grid'):
      if grid:
        grids.append(grid)
      grid = ''
    else:
      grid = grid + l
  if grid:
    grids.append(grid)
  f.close()

  solutions = [solve(grid) for grid in grids]
  for soln in solutions:
    display(soln)
  
  
  print sum(int(''.join(soln[c] for c in cross('A', '123'))) for soln in solutions)