# 17 Table of Numbers
def table(n):
    for i in range(1,11):
        print(f'{n}*{i}= {n*i}')
n=int(input("enter a number : "))
print(f'Table of {n} is {table(n)}')
# 18 Swap of two number
a=int(input('Enter value of a : '))
b=int(input("Enter value of b : "))
print('the original value of a : ',a)
print('the original value of b : ',b)
c=a
a=b
b=c
print('the swaped value of a : ',a)
print('the swaped value of b : ',b)
# 19 check Substring
def sub_str(s1,s2):
    if s2 in s1:
        print(f'{s2} is a substring of {s1}')
    else:
        print(f'{s2} is not a substring of {s1}')
s1=input('Enter a main string : ')
s2=input("Enter a substring : ")
sub_str(s1,s2)

# 20 Decimal to binary
def dec_to_bin(n):
    if n==0:
        return '0'
    binary=[]
    while n>0:
        binary.insert(0,str(n%2))
        n=n//2
    return ''.join(binary)
print(dec_to_bin(5))

# 21 Matrix Addition
def add_matrix(m1,m2):
    if len(m1) !=len(m2) or len(m1[0]) != len(m2[0]):
        return "matrix should have hte same dimension"
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j]+=m2[i][j]
    return m1
m1=[[1,2,3],[4,5,6],[7,8,9]]
m2=[[9,8,7],[6,5,4],[3,2,1]]
print(add_matrix(m1,m2))

# 22 Matrix Multiplicaton
def mul_matrix(m1,m2):
  if len(m1[0]) != len(m2):
    return "Matrix should have the same dimension"
  result = [[0 for i in range(len(m2[0]))] for j in range(len(m1))]
  for i in range(len(m1)):
    for j in range(len(m2[0])):
      for k in range(len(m2)):
        result[i][j] += m1[i][k] * m2[k][j]
  return result
m1 = [[1,2,3],[4,5,6],[7,8,9]]
m2 = [[9,8,7],[6,5,4],[3,2,1]]
print(mul_matrix(m1,m2))

# 23 Find second largent
def second_largest(lst):
  if len(lst)<2:
    return "List should have at least 2 elements"
  lst.sort(reverse=True)
  return lst[1]

lst=[1,2,3,4,5]
print(second_largest(lst))

# 24 check anagram
def anagarm(s1,s2):
  if len(s1) != len(s2):
    return False
  s1=s1.replace(' ',' ').lower()
  s2=s2.replace(' ',' ').lower()
  return sorted(s1)==sorted(s2)
s1=input("Enter 1st string: ")
s2=input("Enter 2nd string: ")
print((anagarm(s1,s2)))


# 3.AI based Tic-Tac-Toe
board = [' ' for _ in range(9)]
def print_board(board):
  for row in range(3):
    print('|' + '|'.join(board[row*3:(row+1)*3]) + '|')

def is_draw(board):
  return all(cell != ' ' for cell in board)

def check_winner(board, player):
  win_combinations = [
      [0, 1, 2], [3, 4, 5], [6, 7, 8],
      [0, 3, 6], [1, 4, 7], [2, 5, 8],
      [0, 4, 8], [2, 4, 6]
  ]
  for condition in win_combinations:
    if all(board[i] == player for i in condition):
      return True
  return False

def minimax(board, depth, is_maximizing):
  if check_winner(board, 'X'):
    return -10 + depth
  if check_winner(board, 'O'):
    return 10 - depth
  if is_draw(board):
    return 0

  if is_maximizing:
    best_score = -float('inf')
    for move in get_available_moves(board):
      board[move] = 'O'
      score = minimax(board, depth + 1, False)
      board[move] = ' '
      best_score = max(score, best_score)
    return best_score
  else:
    best_score = float('inf')
    for move in get_available_moves(board):
      board[move] = 'X'
      score = minimax(board, depth + 1, True)
      board[move] = ' '
      best_score = min(score, best_score)
    return best_score

def get_best_move(board):
  best_score = -float('inf')
  best_move = None
  for move in get_available_moves(board):
    board[move] = 'O'
    score = minimax(board, 0, False)
    board[move] = ' '
    if score > best_score:
      best_score = score
      best_move = move
  return best_move

def get_available_moves(board):
  return [i for i in range(9) if board[i] == ' ']

def play_game():
  global board
  while True:
    print_board(board)
    player_move = int(input("Enter your move (0-8): "))
    if board[player_move] == ' ':
      board[player_move] = 'X'
      if check_winner(board, 'X'):
        print_board(board)
        print("You win!")
        break
      if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break
      ai_move = get_best_move(board)
      board[ai_move] = 'O'
      if check_winner(board, 'O'):
        print_board(board)
        print("AI wins!")
        break
      if is_draw(board):
        print_board(board)
        print("It's a draw!")
        break
    else:
      print("Invalid move. Try again.")
  if input("Play again? (y/n): ").lower() == 'y':
    reset_game()
    play_game()

def reset_game():
  global board
  board = [' ' for _ in range(9)]

play_game()