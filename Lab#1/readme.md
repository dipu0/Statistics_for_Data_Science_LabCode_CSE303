<br>
<div style="font-style: bold; text-align: center;">
<img src="https://www.ewubd.edu/themes/east-west-university/assets/default/images/logo.png" alt="ERROR" title="EWULOGO" width=":5.72917in"/><br>Department of Computer Science & Engineering
<br><br><br>
</div>
<br><br>
<div style="font-style:underline; text-align: center;" markdown="1">

# Lab Report – 1
<br><br>
<br><br>

</div>


<div style="font-style: bold; text-align: left;" markdown="1">

## Semester : Spring 2022

## Course Number : CSE303

## Course Title : Statistics for Data Science

## Course Instructor : Md Al-Imran

<br><br>
<br><br>
<br><br>
<br><br>

## > student ID: 2019-1-60-093
## > Student Name: Md. Asad Chowdhury Dipu
## > Section: 03
## > Date Of Submission: 23/02/2022
<br>
</div>
<br>

# Lab#1


```python
print ("This line will be printed.")
```

    This line will be printed.
    


```python
name = "John"
age = 23
print ("%s is %d years old." % (name, age))
```

    John is 23 years old.
    


```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f'{name} is {age} years old')
```

    Enter your name: Dipu
    Enter your age: 21
    Dipu is 21 years old
    


```python
x=5
print(x)
print(type(x))
```

    5
    <class 'int'>
    


```python
x="hello"
print(x)
print(type(x))
```

    hello
    <class 'str'>
    


```python
import math
print(format(math.pi, '0.12g'))
print(format(math.pi, '0.6f'))
```

    3.14159265359
    3.141593
    


```python
2**52 <= 2**56 // 10 < 2**53
```




    True




```python
# If statement
x = 4
if x < 1:
    score = "low"
elif x <= 4: # elif = else if
    score = "medium"
else:
    score = "high"
print (score)
```

    medium
    


```python
# If statement with a boolean
x = True
if x:
    print ("it worked")
```

    it worked
    


```python
# For loop
veggies = ["carrots", "broccoli", "beans"]
for veggie in veggies:
    if veggie == "broccoli":
        continue
    print(veggie)
```

    carrots
    beans
    


```python
# Creating a list
x = [3, "hello", 1.2
]
print (x)
```

    [3, 'hello', 1.2]
    


```python
# Creating a tuple
x = (3.0, "hello")
# tuples start and end with ()
print (x)
```

    (3.0, 'hello')
    


```python
# Sets
text = "SDS IN PYTHON"
print (set(text))
print (set(text.split(" ")))
```

    {'S', 'P', 'H', 'T', 'N', 'D', ' ', 'I', 'O', 'Y'}
    {'IN', 'SDS', 'PYTHON'}
    


```python
# Grab every letter in string
lst = [x for x in 'word']
lst
```




    ['w', 'o', 'r', 'd']




```python
# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]
lst
```




    [0, 2, 4, 6, 8, 10]




```python
# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius ]
fahrenheit
```




    [32.0, 50.0, 68.18, 94.1]




```python
#nested list comprehension
lst = [ x**2 for x in [x**2 for x in range(11)]]
lst
```




    [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]




```python
phonebook = { "John" : 938477566, "Jack" : 938377264, "Jill" : 947662781 }
print(phonebook)
```

    {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
    


```python
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
```

    Phone number of John is 938477566
    Phone number of Jack is 938377264
    Phone number of Jill is 947662781
    


```python
# Define the function
def add_two(x):
    # explains what this function will do
    x += 2
    return x
```


```python
def f(*args, **kwargs):
    x = args[0]
    y = kwargs.get("y")
    print (f"x: {x}, y: {y}")
f(5, y=2)
```

    x: 5, y: 2
    


```python
veggies = ["Beans", "Broc", "Ban"]
for veggie in veggies:
    if "Broc" in veggie:
        continue
    print(veggie)
```

    Beans
    Ban
    


```python
# Creating the class
class Pet(object):
    def __init__(self, species, name):
        self.species = species
        self.name = name
        
```


```python
# Creating an instance of a class
my_dog = Pet(species="dog",
    name="Scooby")

print (my_dog)
print (my_dog.name)
```

    <__main__.Pet object at 0x000001C0C3099820>
    Scooby
    


```python
# Creating the class
class Pet(object):
    def __init__(self, species, name):
        self.species = species
        self.name = name
    def __str__(self):
        return f"{self.species} named {self.name}"
```


```python
# Creating an instance of a class
my_dog = Pet(species="dog",
    name="Scooby")

print (my_dog)
print (my_dog.name)
```

    dog named Scooby
    Scooby
    


```python
# Creating the class
class Pet(object):
    def __init__(self, species, name):
        self.species = species
        self.name = name
    def __str__(self):
        return f"{self.species} named {self.name}"
    def change_name(self, new_name):
        self.name = new_name
```


```python
# Creating an instance of a class
my_dog = Pet(species="dog", name="Scooby")
print (my_dog)
print (my_dog.name)
```

    dog named Scooby
    Scooby
    


```python
# Using a class's function
my_dog.change_name(new_name="Scrappy")
print (my_dog)
print (my_dog.name)
```

    dog named Scrappy
    Scrappy
    


```python
#Inheritance
class Dog(Pet):
    def __init__(self, name, breed):
        super().__init__(species="dog", name=name)
        self.breed = breed
    def __str__(self):
        return f"A {self.breed} doggo named {self.name}"

scooby = Dog(breed="Great Dane", name="Scooby")
print (scooby)
```

    A Great Dane doggo named Scooby
    


```python
scooby.change_name("Scooby Doo")
print (scooby)
```

    A Great Dane doggo named Scooby Doo
    

# Exercise

1. Given two integer numbers, write a Python program to return their product. If the product is greater
than 1000, then return their sum. Read inputs from the user.


```python
def action(x1,x2):
    if(x1*x2 < 1000):
        print("Product is: ")
        return x1*x2
    else:
        print("Product is less than 1000 so the sum of x1 & x2 : ")
        return x1+x2
    
x1 = int(input('Enter number x1: '))
x2 = int(input('Enter number x2: '))

print(action(x1,x2))
```

    Product is less than 1000 so the sum of x1 & x2 : 
    201
    

2. Write a Python program to find the area and perimeter of a circle. Read inputs from the user.


```python
import math

def circle(radius):
    area = math.pi*(radius*radius)
    print("Area of the circle is : ",area)
    perimeter = 2*math.pi*radius
    print("Perimeter of the circle is : ",perimeter)

radius= int(input("Enter the radius of the circle: "))
circle(radius)
```

    Area of the circle is :  78.53981633974483
    Perimeter of the circle is :  31.41592653589793
    

3. Write a Python program to calculate the compound interest based on the given formula. Read inputs
from the user.

A = P * (1 + R/100)^T
where P is the principle amount, R is the interest rate and T is time (in years).

Define a function named as compound_interest_< your-student-id > in your program.


```python
def compound_interest_2019_1_60_093(P,R,T):
    return P * ((1 + R/100)**T)

P=int(input("Enter the principle amount:  "))

R= float(input("Enter the interest rate: "))

T= int(input("Enter the time(in years): "))

A= compound_interest_2019_1_60_093(P,R,T)

print("Compound interest is : ",A)
```

    Enter the principle amount:  23000
    Enter the interest rate: 10.5
    Enter the time(in years): 1
    Compound interest is :  25415.0
    

4. Given a positive integer N (read from the user), write a Python program to calculate the value of the
following series.
1^2 + 2^2 + 3^2 + 4^2 .. .... +N^2


```python
def calculate_Value(N):
    return (N*(N+1)*(2*N+1))/6

N=int(input("Enter a number : "))

a=calculate_Value(N)

print("Value of the following series: ",a)

```

    Enter a number : 6
    Value of the following series:  91.0
    

5. Given a positive integer N (read from the user), write a Python program to check if the number is
prime or not. Define a function named as prime_find_<your-student-id> in your program.


```python
def prime_find_2019_1_60_093(num):
    if num> 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                print("It's not a prime number")
        print("It's a prime number")
    else:
        print("It's not a prime number")
    
n=int(input("Enter a number: "))

prime_find_2019_1_60_093(n)
```

    Enter a number: 1
    It's not a prime number
    

6. Given a positive integer n (read from the user), write a Python program to find the n-th Fibonacci
number based on the following assumptions.
Fn = Fn-1 + Fn-2 where F0 = 0 and F1 = 1


```python
def fibonacci(n):
    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter a number: "))

print(n,"th fibonacci number is : ",fibonacci(n))
```

    Enter a number: 6
    6 th fibonacci number is :  8
    

7. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
the list. Do not use any built-in function.


```python
list = [0,1,5,2,1,5,8,3,5,3,4]
def do_sum(list):
    sum=0 
    for x in list:
        sum+=x    
    return sum

print(do_sum(list))
```

    37
    

8. Given a list of numbers (hardcoded in the program), write a Python program to calculate the sum of
the even-indexed elements in the list.


```python
list = [0,1,5,2,1,5,8,3,5,3,4]
def do_sum(list):
    sum=0 
    for i in range(len(list)):
        if(i%2==0):
            sum+=list[i]
    return sum

print(do_sum(list))
```

    23
    

9. Given a list of numbers (hardcoded in the program), write a Python program to find the largest and
smallest element of the list. Define two functions largest_number_< your-student-id > and
smallest_number_< your-student-id > in your program. Do not use any built-in function.


```python
list = [0,1,5,2,1,5,8,3,5,3,4]

def largest_number_2019_1_60_093(list):
    max = -99999
    for x in list:
        if x > max:
            max=x
    return max
def smallest_number_2019_1_60_093(list):
    min = 99999
    for x in list:
        if x < min:
            min = x
    return min
print("largest number: ",largest_number_2019_1_60_093(list), "smallest number: ",smallest_number_2019_1_60_093(list))
```

    largest number:  8 smallest number:  0
    

10. Given a list of numbers (hardcoded in the program), write a Python program to find the second
largest element of the list.


```python
list = [0,1,5,2,1,5,8,3,5,3,4]
list.sort()
print("second largest number: ", list[len(list)-2])
```

    second largest number:  5
    

11. Given a string, display only those characters which are present at an even index number. Read inputs
from the user.


```python
string=input("Enter a string : ")
print("Characters present at an even index number are : ")
for i in range(len(string)):
    if i%2==0:
        print(string[i] ,end="")
```

    Enter a string : Welcome to CSE303
    Characters present at an even index number are : 
    Wloet S33

12. Given a string and an integer number n, remove characters from a string starting from zero up to n
and return a new string. N must be less than the length of the string. Read inputs from the user. Do
not use any built-in function.


```python
string=input("Enter a string: ")

N=int(input("Enter a number = "))

new_string=""
i=0

for i in range(len(string)):
    if i>=N:
        new_string=new_string+string[i]

print("New string is : ",new_string)
```

    Enter a string: hello world
    Enter a number = 3
    New string is :  lo world
    

13. Given a string, find the count of the substring “CSE303” appeared in the given string. Do not use any
built-in function.


```python
string = 'CSE303 must be done before CSE366. Otherwise CSE303 will be dropped.'
substring="CSE303"

def count_substring(string,substring):
    count=0
    for x in string.split():
        if x == substring:
            count+=1
    return count
print("The no of substring appeared: ",count_substring(string, substring))
```

    The no of substring appeared:  2
    

14. Given a string, write a python program to check if it is palindrome or not. Define a function named
palindrome_checker_< your-student-id > in your program.


```python
string= input("Enter a string :")

def palindrome_checker_2019_1_60_093(string):
    s = ""
    for i in string:
        s = i + s
    print(s)
    if string==s:
        print("Palindrome")
    else:
        print("Not a palindrome")

palindrome_checker_2019_1_60_093(string)
```

    Enter a string :mom
    mom
    Palindrome
    

15. Given a two list of numbers (hardcoded in the program), create a new list such that new list should
contain only odd numbers from the first list and even numbers from the second list.


```python
list1=[0,1,5,2,1,5,8,3,5,3,4]
list2=[0,1,3,0,6,9,9,9,0,0,5]

even=[]
odd=[]
new_list=[]

def extract_new_list(list1,list2):
    for i in list1:
        if i%2!=0:
            odd.append(i)
            new_list.append(i)
    print("Odd numbers from list1 :",odd)
    
    for i in list2:
        if i%2==0:
            even.append(i)
            new_list.append(i)
    print("Even numbers from list 2 :",even)
    
    print("New List: ",new_list)
    
    return new_list
    
extract_new_list(list1,list2)
```

    Odd numbers from list1 : [1, 5, 1, 5, 3, 5, 3]
    Even numbers from list 2 : [0, 0, 6, 0, 0]
    New List:  [1, 5, 1, 5, 3, 5, 3, 0, 0, 6, 0, 0]
    




    [1, 5, 1, 5, 3, 5, 3, 0, 0, 6, 0, 0]


