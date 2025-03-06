# 33 Task find all permutation of a string
from itertools import permutations
def string_permutations(s):
    return [''.join(p)for p in permutations(s)]

print(string_permutations('123'))

# 34 Task N-th fibonacci number (dynamic programming)
def fibonacci(n):
    fib=[0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
print(fibonacci(10))
# Task 35 find duplicates in a list
from collections import Counter
def find_duplicates(lst):
    counts=Counter(lst)
    return [num for num, count in counts.items() if count >1]
print(find_duplicates([1,2,3,4,5,2,3,6,7,8,8]))
# Task 36 longest increasing subsequence
def longest_increasing_subsequence(arr):
    n=len(arr)
    lis=[1]*n
    for i in range(1,n):
        for j in range(i):
            if arr[i]>arr[j]:
                lis[i]=max(lis[i],lis[j]+1)
    return max(lis)
print(longest_increasing_subsequence([10,22,9,33,21,50,41,60,80]))

# Task 37 find k largest element
import heapq
def k_largest_elements(lst,k):
    return heapq.nlargest(k,lst)
print(k_largest_elements([10,5,20,8,30,15],3))

# Task 38 Rotate Matrix
def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
rotated=rotate_matrix(matrix)
for row in rotated:
    print(row)
# Task 39 sudoku validator
def is_valid_suduko(board):
    def is_valid_unit(unit):
        unit=[num for num in unit if num !="."]
        return len(unit)== len(set(unit))
    for row in board:
        if not is_valid_unit(row):
            return False
    for col in zip(*board):
        if not is_valid_unit(col):
            return False
    for i in range(0,9,3):
        for j in range(0,9,3):
            block=[board[x][y] for x in range(i,i+3) for y in range(j,j+3)]
            if not is_valid_unit(block):
                return False
    return True
suduko_board=[
    ['5','3','.','.','7','.','.','.','.'],
    ['6','.','.','1','9','5','.','.','.'],
    ['.','9','8','.','.','.','.','6','.'],
    ['8','.','.','.','6','.','.','.','3'],
    ['4','.','.','8','.','3','.','.','1'],
    ['7','.','.','.','2','.','.','.','6'],
    ['.','6','.','.','.','.','2','8','.'],
    ['.','.','.','4','1','9','.','.','5'],
    ['.','.','.','.','8','.','.','7','9'],
]
print(is_valid_suduko(suduko_board))

# 5 Virtual stock Market simulator
import random

class StockMarketSimulator:
    def __init__(self):
        self.stocks={'AAPL':150,'GOOG':2800,'TSLA':700}
        self.portfolio={}

    def update_price(self):
        for stock in self.stocks:
            self.stocks[stock]+=random.randint(-5,5)

    def buy_stock(self,stock,quantity):
        if stock in self.stocks:
            cost=self.stocks[stock]*quantity
            self.portfolio[stock]=self.portfolio.get(stock,0)+quantity
            print(f'Bounght {quantity} shares of {stock} for ${cost}')

    def sell_stock(self,stock,quantity):
        if stock in self.portfolio and self.portfolio[stock]>=quantity:
            revenue=self.stocks[stock]*quantity
            self.portfolio[stock]-=quantity
            print(f'Sold {quantity} share of {stock} for ${revenue}')

    def display_market(self):
        print('stock Price:',self.stocks)

market=StockMarketSimulator()
market.display_market()
market.buy_stock('AAPL',10)
market.update_price()
market.display_market()
market.sell_stock('AAPL',5)    