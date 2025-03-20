# task 40 word frequency in text
from collections import Counter 
def word_frequency(text):
    words=text.lower().split()
    return dict(Counter(words))
text='this is a sample text.this text is for counting words.'
print(word_frequency(text))

# Task 41 knapsack problem
def knapsack(weights,values,capacity):
    n=len(weights)
    dp=[[0 for _ in range(capacity +1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,capacity+1):
            if weights[i-1]<=w:
                dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]
    return dp[n][capacity]
weights=[2,3,4,5]
values=[3,4,5,6]
capacity=5
print(knapsack(weights,values,capacity))

# Task 42 Merge interval
def merge_interval(intervals):
    intervals.sort()
    merged=[intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1]=max(merged[-1][1],end)
        else:
            merged.append([start,end])
    return merged
intervals=[[1,3],[2,6],[8,10],[15,18]]
print(merge_interval(intervals))

# Task 43 find the median of two sorted arrays
import statistics
def find_median(arr1,arr2):
    merged=sorted(arr1+arr2)
    return statistics.median(merged)
arr1=[1,3]
arr2=[2]
print(find_median(arr1,arr2))
# Task 44 MAximal rectangle in binary matrix
def maximal_rectangle(matrix):
    if not matrix:
        return 0
    max_area=0
    heights=[0]*len(matrix[0])
    for row in matrix:
        for i in range(len(row)):
            heights[i]=heights[i]+1 if row[i]=='1' else 0
        max_area=max(max_area,max_histogram_area(heights))
    return max_area

def max_histogram_area(heights):
    stack, max_area=[],0
    for i ,h in enumerate(heights+[0]):
        while stack and heights[stack[-1]]>h:
            height=heights[stack.pop()]
            width=i if not stack else i-stack[-1]-1
            max_area=max(max_area,height*width)
        stack.append(i)
    return max_area
matrix=[
    ['1','0','1','0','0'],
    ['1','0','1','1','1'],
    ['1','1','1','1','1'],
    ['1','0','0','1','0']
]
print(maximal_rectangle(matrix))

# Task 45 find largest sum contigious subarray(kadane's Algorithm)
def max_subarray_sum(arr):
    max_sum=curr_sum=arr[0]
    for num in arr[1:]:
        curr_sum=max(num,curr_sum+num)
        max_sum=max(max_sum,curr_sum)
    return max_sum
arr=[-2,1,-3,4,-1,2,1,-5,4]
print(max_subarray_sum(arr))

# project 6 command-line RPG Game
import random 
class Character:
    def __init__(self,name,health,attack):
        self.name=name
        self.health=health
        self.attack=attack

    def attack_enemy(self,enemy):
        damage=random.randint(1,self.attack)
        enemy.health-=damage
        print(f'{self.name} attack {enemy.name} for {damage} damage')

player=Character('Hero',100,15)
enemy=Character('Goblin',50,10)

while enemy.health >0 and player.health >0:
    player.attack_enemy(enemy)
    if enemy.health<=0:
        print(f'{enemy.name} is dafeated!')
        break
    enemy.attack_enemy(player)

print('Game Over')