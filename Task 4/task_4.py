# 25 Find missing number
def missing(lst,n):
    sum_lst=0
    for i in lst:
        sum_lst+=i
    num=(n*(n+1))//2
    missing_num=num-sum_lst
    print(lst)
    print(f'the missing number is: {missing_num}')
lst=[1,2,4,6,3,7,8]
n=len(lst)+1
missing(lst,n)
# 26 is_balanced
def is_balanced(s):
    stack=[]
    mapping={')':'(','}':'{',']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or mapping[char] != stack.pop():
                return False
    return not stack
s="{[()]}"
print(f'Is balanced: {is_balanced(s)}')
# 27 Check balanced parenthesis
def longest_word(sentence):
    words=sentence.split()
    longest_word=max(words,key=len)
    return longest_word
    # longest_word=''
    # for word in words: 
    #     if len(word)>len(longest_word):
    #         longest_word=word
    # return longest_word
sentence='this is longest sentence'
print(f'this is the longest word : {longest_word(sentence)}')

# 28 Count word in sentence
def count_word(sentence):
    words=sentence.split()
    count=0
    for i in words:
        count+=1
    return count
sentence='this is so easy'
print(f'number of words in sentence is : {count_word(sentence)}')
# 29 check pythagorean triplet
# type 1 solution
def pytha_triplet(a,b,c):
    a,b,c=sorted([a,b,c])
    return a**2+b**2==c**2
a,b,c=3,4,5
print(f'Is pythagorean Triplet : {pytha_triplet(a,b,c)}')
# type 2 solution
def pytha_triplet(a,b,c):
    a2=a**2
    b2=b**2
    c2=c**2
    if a2+b2==c2:
        return True
    else:
        return False
    # print(a2+b2) 
print(f'Is pythagorean triplet : {pytha_triplet(3,4,5)}')
# 30 Bubble sort
def bubble_sort(lst):
    n=len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1]=lst[j+1],lst[j]
    return lst
lst=[21,41,52,29,67,15,80]
print(f'Sorted list is : {bubble_sort(lst)}')

# 31 Binary serach 
def binary_search(lst,target):
    left,right=0,len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]==target:
            return mid
        elif lst[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
lst=[1,2,3,4,5,6,7,8,9,10]
target=7
print(f'Index of {target} is : {binary_search(lst,target)}')

# # 32.Find Subarray with Given Sum
def subarray_sum(lst, target):
  current_sum = 0
  start = 0
  for end in range(len(lst)):
    current_sum += lst[end]
    while current_sum > target:
      current_sum -= lst[start]
      start += 1
    if current_sum == target:
      return start, end
  return -1

lst = [1, 2, 3, 7, 5]
target = 12
print(f"Subarray with given sum: {subarray_sum(lst, target)}")
# 4. Analysis System
def analysis_logs(file_path):
    ip_count={}
    with open(file_path,'r') as file:
        for line in file:
            parts=line.split()
            if len(parts)>0:
                ip=parts[0]
                ip_count[ip]=ip_count.get(ip,0)+1
    sorted_ips=sorted(ip_count.items(),key=lambda x:x[1],reverse=True)
    return sorted_ips[:5] #return top 5 most frequent Ips
# Assume 'server_logs.txt is in the current directory
# create a small log file for demonstration 
with open("server_logs.txt", "w") as file:
  file.write("192.168.1.1 - - [12/Jul/2023] GET /index.html 200\n")
  file.write("192.168.1.2 - - [12/Jul/2023] GET /about.html 200\n")
  file.write("192.168.1.1 - - [12/Jul/2023] GET /contact.html 404\n")
  file.write("192.168.1.3 - - [12/Jul/2023] GET /index.html 200\n")
  file.write("192.168.1.2 - - [12/Jul/2023] GET /home.html 200\n")
print("Top IP addresses: ")
print(analysis_logs("server_logs.txt"))