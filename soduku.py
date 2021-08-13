board = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]
def solve(brd):
  finder = findemp(brd)
  if not finder:
    return True
  else:
    r, c = finder
  for i in range(1, 10):
    if isvalid(brd, i, (r, c)):
      brd[r][c] = i
 
      if solve(brd):
        return True
      brd[r][c] = 0 
  return False
 
 
 
 
 
def isvalid(brd, n, p):
  for i in range(len(brd[0])):
    if brd[p[0]][i] == n and p[1] != i:
      return False
  for i in range(len(brd)):
    if brd[i][p[1]] == n and p[1] != i:
      return False
  bx = p[1] // 3
  by = p[0] // 3
  for i in range(by*3, by * 3 + 3):
    for t in range(bx* 3, bx * 3 + 3):
      if brd[i][t] == n and (i, t) != p:
        return False
  return True
 
 
def printb(brd):
  for i in range(len(brd)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - -")
    for t in range(len(brd[0])):
      if t % 3 == 0 and t != 0:
        print(" | ", end = "")
      if t == 8:
        print(brd[i][t])
      else:
        print(str(brd[i][t]) + " ", end="")
def findemp(brd):
  for i in range(len(brd)):
    for t in range(len(brd[0])):
      if brd[i][t] == 0:
        return (i, t)
  return None
 
solve(board)
printb(board)