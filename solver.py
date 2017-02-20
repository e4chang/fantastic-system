import random
N_ROWS = 5
N_COLS = 6

class Node:
  def __init__(self, x_index, y_index):
    self.x = x_index
    self.y = y_index

class Board:
  def __init__(self):
    self.b = [[0 for j in range(N_COLS)] for i in range(N_ROWS)]
    self.current= 0
  def __repr__(self):
    return repr(self.b)
  
  def __iter__(self):
    return self

  def next(self):
    if self.current >= N_ROWS:
      raise StopIteration
    else:
      self.current += 1
      return self.b[self.current - 1]

  def copyBoard(self, board):
    for i in range(N_ROWS):
      for j in range(N_COLS):
        self.b[i][j] = board[i][j]

# Helper function to count the number of 1's on the board
def count1(board):
  return sum(map(sum, board))

# Helper function to import optimal boards
def importBoards(fname):
  boards = []
  with open(fname, 'r') as inputFile:
    nBoards = int(next(inputFile))
    for i in range(nBoards):
      data = []
      for j in range(N_ROWS):
        row = next(inputFile)
        data.append(map(int, row.split()))
      board = Board()
      board.copyBoard(data)
      boards.append(board)
  return boards

       
x = Node(5,6)

# Generate a random 5x6 board with two colors
def generateBoard():
  nBoards = 1

  board = [[0 if random.random() < 0.5 else 1 for j in range(N_COLS)] for i in range(N_ROWS)]
  with open('input.txt', 'w') as outputFile: 
    outputFile.write(str(nBoards) + '\n')
    for i in range(N_ROWS):
      outputFile.write(' '.join(map(str,board[i])))
      outputFile.write('\n')

generateBoard()
game = importBoards('input.txt')

print count1(game[0])
optimals = importBoards('optimal.txt')
optimalBoard = { count1(b) : b for b in optimals }
