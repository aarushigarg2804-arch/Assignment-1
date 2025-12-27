Python 3.14.1 (tags/v3.14.1:57e0d17, Dec  2 2025, 14:05:07) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Assignment 1
#input
\
>>> #1
>>> num1 = input("Enter a number:")
Enter a number:30
>>> num2 = input("Enter another number here:")
Enter another number here:25
>>> #2
>>> addition=int(num1)+int(num2)
>>> print(addition)
55
>>> subtraction=int(num1)-int(num2)
>>> print(subtraction)
5
>>> multiplication=int(num1)*int(num2)
>>> print(multiplication)
750
>>> division=int(num1)/int(num2)
>>> print(division)
1.2
>>> #Task--2
>>> first_name=input("Write first name here-")
Write first name here-John
>>> Last_name=input("Write last name here-")
Write last name here-Doe
>>> print( "Hello,", First_name, Last_name, "! Welcome to Python Program")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print( "Hello,", First_name, Last_name, "! Welcome to Python Program")
NameError: name 'First_name' is not defined. Did you mean: 'first_name'?
>>> print("Hello,", first_name, Last_name, "! Welcome to Python Program")
Hello, John Doe ! Welcome to Python Program
>>> print(first_name, Last_name)
John Doe
