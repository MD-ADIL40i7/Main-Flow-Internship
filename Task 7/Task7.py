# Task 47 Count Inversion in array
def merge_and_count(arr,temp_arr,left,mid,right):
    i,j,k=left,mid+1,left
    inv_count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            i+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=(mid-i+1)
            j+=1
        k+=1
    while i<=mid:
        temp_arr[k]=arr[i]
        i+=1
        k+=1
    while j<=right:
        temp_arr[k]=arr[j]
        j+=1
        k+=1 
    for i in range(left,right+1):
        arr[i]=temp_arr[i]
    return inv_count
def merge_sort(arr,temp_arr,left,right):
    inv_count=0
    if left<right:
        mid=(left+right)//2
        inv_count+=merge_sort(arr,temp_arr,left,mid)
        inv_count+=merge_sort(arr,temp_arr,mid+1,right)
        inv_count+=merge_and_count(arr,temp_arr,left,mid,right)
    return inv_count
def count_inversions(arr):
    temp_arr=[0]*len(arr)
    return merge_sort(arr,temp_arr,0,len(arr)-1)
arr=[1, 20, 6, 4, 5]
print('NUmber of invasions:' , count_inversions(arr))

# Task 48 Longest paliondrome substring
def longest_palindrome_sunstring(s):
    def expand_around_center(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    longest=''
    for i in range(len(s)):
        odd_palindrome=expand_around_center(i,i)
        even_palindrome=expand_around_center(i,i+1)
        longest=max(longest,odd_palindrome,even_palindrome,key=len)
    return longest
print(longest_palindrome_sunstring('babad'))
# Task 49 Travelling salesman Problem(TSP)
from itertools import permutations
def tsp(graph,start):
    n=len(graph)
    vertices=[i for i in range(n) if i != start]
    min_path=float('inf')

    for perm in permutations(vertices):
        current_path_weight=0
        k=start
        for j in perm:
            current_path_weight+=graph[k][j]
            k=j
        current_path_weight+=graph[k][start]
        min_path=min(min_path,current_path_weight)
    return min_path
graph=[
    [0,29,20,21],
    [29,0,15,17],
    [20,15,0,28],
    [21,17,28,0]
]
print('shortest TSP rout cost: ',tsp(graph,0))

# Task 50 graph cycle detection
def dfs(graph,v,visited,parent):
    visited[v]=True
    for neighbour in graph[v]:
        if not visited[neighbour]:
            if dfs(graph,neighbour,visited,v):
                return True
        elif parent != neighbour:
            return True
    return False

def contains_cycle(graph):
    visited={node:False for node in graph}
    for node in graph:
        if not visited[node]:
            if dfs(graph,node,visited,-1):
                return True
    return False
graph={0:[1,2],1:[0,3],2:[0,3],3:[1,2]}
print('Cycle present: ',contains_cycle(graph))

# Task 51 longest substring without repeating characters
def longest_unique_substring(s):
    char_map={}
    left=max_lenght=0
    for right, char in enumerate(s):
        if char in char_map and char_map[char]>=left:
            left=char_map[char]+1
        char_map[char]=right
        max_lenght=max(max_lenght,right-left+1)
    return max_lenght
print(longest_unique_substring('abcabcbb'))

# Task 52 generate All valid prentheses combination
def genarate_parentheses(n):
    def backtrack(s,open_count,close_count):
        if len(s)==2*n:
            result.append(s)
            return
        if open_count<n:
            backtrack(s+'(',open_count+1,close_count)
        if close_count<open_count:
            backtrack(s+')',open_count,close_count+1)
    result=[]
    backtrack('',0,0)
    return result
n=3
print('valid paranthesis combination: ',genarate_parentheses(n))
# Task 53 Zigzag level order Traversal of a binary tree
from collections import deque
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def zigzag_level_order(root):
    if not root:
        return[]
    result,queue,left_to_right=[],deque([root]),True
    while queue:
        level_size=len(queue)
        level=deque()
        for _ in range(level_size):
            node =queue.popleft()
            if left_to_right:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        left_to_right=not left_to_right
    return result
# example Tree
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(7)
print("zigzag level order Traversal: ",zigzag_level_order(root))

# Task 54 Palindrome partitioning
def palindrome_paratitioning(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    def backtrack(start,path):
        if start==len(s):
            result.append(path[:])
            return
        for end in range(start+1,len(s)+1):
            if is_palindrome(s[start:end]):
                backtrack(end,path+[s[start:end]])
    result=[]
    backtrack(0,[])
    return result
# example
s='aab'
print("palindrome Partition:",palindrome_paratitioning(s))

# project 7 personal budget advisor project
class BudgetAdvisor:
    def __init__(self,income):
        self.income=income
        self.expenses={}
    def add_expense(self,category,amount):
        if category in self.expenses:
            self.expenses[category]+=amount
        else:
            self.expenses[category]=amount

    def get_summary(self):
        total_expenses=sum(self.expenses.values())
        saving=self.income-total_expenses
        print(f'Total Income: $ {self.income}')
        print(f'Total Expenses: $ {total_expenses}')
        print(f'saving: $ {saving}')

        for category,amount in self.expenses.items():
            percentage=(amount/self.income)*100
            print(f'{category}:${amount} ({percentage:2f}%)')
        if saving <0:
            print('Warning : You are overspending')

advisor=BudgetAdvisor(3000)
advisor.add_expense('Rent',1200)
advisor.add_expense("food",500)
advisor.add_expense("entertainment",300)
advisor.get_summary()