#9 prime number
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("enter a number: "))
if prime(n):
    print(n,'is a prime number')
else:
    print(n,'is not a prime number')

# 10 Sum of digits
def sum(n):
    str_n=str(n)
    sum_digits=0
    for char in str_n:
        sum_digits +=int(char)
    return sum_digits
n=int(input('Enter a number: '))
print('sum of digits:',sum(n))

# 11 LCM and GCD
import math
def lcm_and_gcd(a,b):
    gcd=math.gcd(a,b)
    lcm=abs(a*b)//gcd
    return lcm,gcd
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
lcm,gcd=lcm_and_gcd(a,b)
print('LCM:',lcm)
print('GCD:',gcd)

# 12 List Reversal
def reversal_list(lst):
    n=len(lst)
    for i in range(n//2):
        lst[i],lst[n-i-1]=lst[n-i-1],lst[i]
    return lst
lst=[]
n=int(input("enter the number of elements in the list: "))
for i in range(n):
    ele=int(input('enter element: '))
    lst.append(ele)
print('Original list:',lst)
print('Reversed list:',reversal_list(lst))

# 13 sort list
def bubble_sort(lst):
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[]
n=int(input("Enter the number of element "))
for i in range(n):
    ele=int(input("enter the element: "))
    lst.append(ele)
print("Original list:",lst)
print("Reversed list: ",bubble_sort(lst))
# 14 Remove Duplicate
def remove_duplicate(lst):
    return list(set(lst))
lst=[]
n=int(input("enter the number of element: "))
for i in range(n):
    ele=int(input("Enter element: "))
    lst.append(ele)
print("original list: ",lst)
print("list after removing duplicate: ",remove_duplicate(lst))
# 15 String Length
def string_lenght(str):
    return len(str)
str=input("enter a string: ")
print('lenght of string is :',string_lenght(str))

# 16 count vowel and consonants
def vowels_consonant(s):
    vowels='aeiouAEIOU'
    v_count=0
    c_count=0
    for char in s :
        if char.isalpha():
            if char in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count
s=input("Enter a string: ")
v_count,c_count=vowels_consonant(s)
print("number of vowels: ",v_count)
print('number of consonants: ',c_count)

# 17 Maze Generator and solver
from collections import deque
def bfs(maze,start,goal):
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    queue=deque([start])
    visited=set([start])
    parent={start:None}
    while queue:
        current=queue.popleft()

        if current==goal:
            path=[]
            while current:
                path.append(current)
                current=parent[current]
            return path[ : :-1]
        for direction in directions:
            r, c=current[0]+direction[0],current[1]+direction[1]
            if 0<= r < len(maze) and 0 <=c <len(maze[0]) and maze[r][c]==0 and(r,c) not in visited:
                queue.append((r,c))
                visited.add((r,c))
                parent[(r,c)]=current 
    return None
def print_maze_with_path(maze,path):
    for r,c in path:
        if (r,c) !=path[0] and (r,c) !=path[-1]:
            maze[r][c]=2
    for row in maze:
        print(' '.join(['#' if cell ==1 else '.' if cell==0 else 'p' for cell in row]))
maze=[
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start=(0,0)
goal=(4,4)
path=bfs(maze,start,goal)
if path:
    print('path found: ',path)
    print('Maze with path: ')
    print_maze_with_path(maze,path)
else:
    print("no path found")