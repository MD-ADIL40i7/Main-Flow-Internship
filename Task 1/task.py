# Main-Flow-Internship
# Internship Task 1
# uncomment code to run

# Task 1: sum of two number
# def sum(a,b):
#     add=a+b
#     print(f"the sum of {a} and {b} is :",add)
# a=int(input("enter value of a : "))
# b=int(input('Enter value of b : '))
# sum(a,b)


# Task 2: Odd or even
# def Odd_or_even(n):
#     return 'even' if n%2 == 0 else 'odd' 
# n=int(input('enter the value : '))
# print(f'the number is {n} is {Odd_or_even(n)}')

# Task 3:Find the factorial of a number
# type 1 solution

# def factorial(num):
#     n=1
#     for i in range(1,num+1):
#         n *=i
#     return n
# num=int(input('Enter the number : '))
# print(f'The factorail of {num} is {factorial(num)}.')

# type 2 solution 
# def factorial(num):
#     n=1
#     for i in range(1,num+1):
#         n *=i
#     return n
# q=input('to check factorial entre y or press E : ')
# if q=='y' :
#     num=int(input('Enter the number : '))
#     print(f'The factorial of {num} is {factorial(num)}.')
# else: 
#     print('thank you for using')

# task 4 fibonacci sequesnce
# Type 1 solution
# def fibonacci(n):
#     sequence=[0,1]
#     for i in range(2,n):
#         print( '1')
#         sequence.append(sequence[-1]+sequence[-2])
#     return sequence[0:]
# n=int(input('Enter the length of sequence : '))
# print(f'The first {n} fibonacci number are {fibonacci(n)}.')

# Type 2 solution
# def fibonacci(n):
#     series=[0,1]
#     for i in range(2,n):
#         s=series[-1]+series[-2]
#         series.append(s)
#     return (series[ 0: ])
# n=int(input('Enter the number : '))
# print(f'First {n} fibonacci number are {fibonacci(n)}')

# Task 5 Reverse a string
# def reverse_string(s):
#     return s[ ::-1 ]
# s=input("enter the string : ")
# print(f'the reverse of {s} is {reverse_string(s)}')

# Task 6 palindrome check
# def is_palindrome(p):
#     return p==p[::-1]
# p=input('Enter the string')
# print(f'the string {p} is palindrome ? {is_palindrome(p)}')

# Task 7 leap year
# Type 1 solution
# def leap_year(year):
#     return year%4==0 and(year%100!=0 or year%400==0)
# year=int(input("enter the year : "))
# print(f'the year {year} is leap year ? {leap_year(year)}')
# Type 2 solution
# def leap_year(year):
#     if year%4==0 and (year %100 !=0 or year % 400 ==0) :
#         print('it is a leap year')
#     else:
#         print('it is not a leap year')
# year=int(input('enter the year'))
# leap_year(year)

# Task 8 Armstrong number
# def is_armstrong(n):
#     digits=str(n)
#     return n==sum(int(d)**len(digits) for d in digits)
# num=153
# print(f'Is {num} is a Armstrong number ?{is_armstrong(num)}')

# Type 2 solution
# def is_armstrong(n):
#     digits=str(n)
#     d=0
#     for i in digits:
#         arm =int(i)**len(digits)
#         d += arm
#     if d==n:
#         print(f'{n} is a Armstrong number.')
#     else:
#         print(f'{n} is not a Armstrong number.')
# n=int(input('Enter the number : '))
# is_armstrong(n)

# Custom Encryption-decrytion system
# def encrypt(text,shift):
#     encrypted_text=''
#     for char in text:
#         if char.isalpha():
#             shift_base=65 if char.isupper() else 97
#             encrypted_text += chr((ord(char)-shift_base+shift)%26+shift_base)
#         else:                         
#             encrypted_text += char
#     return encrypted_text

# def decrypt(encrypted_text,shift):
#     return encrypt(encrypted_text,-shift)

# message='Adil bhole'
# shift_key=3

# encrypted_message=encrypt(message,shift_key)
# decrypted_message=decrypt(encrypted_message,shift_key)
# print(f'Original : {message} .')
# print(f'Encrypted : {encrypted_message} .')
# print(f'Decrypted : {decrypted_message} .')
