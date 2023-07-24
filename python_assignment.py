#Programs on selection and Iteration operations. 
#Get an integer input from a user. If the number is odd, then find the factorial of a number and find the number of digits in the factorial of the number. If the number is even, then check the given number is palindrome or not. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def count_digits(num):
    return len(str(num))

num = int(input("Enter an integer: "))

# Check if the number is odd or even
if num % 2 == 1:
    fact = factorial(num)
    digit_count = count_digits(fact)
    print("Factorial:", fact)
    print("Number of digits in factorial:", digit_count)
else:
    if is_palindrome(num):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")




        
#Strings and its operations. 
#Given two strings, PRINT (YES or NO) whether the second string can be obtained from the first by deletion of none, one or more characters.
def can_obtain_string(string1, string2):
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            j += 1
        i += 1

    return j == len(string2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first
if can_obtain_string(string1, string2):
    print("YES")
else:
    print("NO")
def can_obtain_string(string1, string2):
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            j += 1
        i += 1

    return j == len(string2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first
if can_obtain_string(string1, string2):
    print("YES")
else:
    print("NO")





    
#List and its operations
#a) Programs for negative and positive indexing
def indexing_demo(lst):
    # Accessing elements using positive indexing
    print("Positive indexing:")
    for i in range(len(lst)):
        print("Element at index", i, ":", lst[i])

    # Accessing elements using negative indexing
    print("\nNegative indexing:")
    for i in range(-1, -len(lst) - 1, -1):
        print("Element at index", i, ":", lst[i])
#b)Program to check if the given list is ascending order or not
def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

input_list = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in input_list]

# Check if the list is in ascending order
if is_ascending(numbers):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")









#tuples and its operations
#a)  Python program to convert a tuple to a string
def tuple_to_string(tup):
    string = ''.join(tup)
    return string


my_tuple = ('H', 'e', 'l', 'l', 'o')
result = tuple_to_string(my_tuple)
print("Converted string:", result)



#b) Python program to reverse a tuple
def reverse_tuple(tup):
    reversed_tuple = tuple(reversed(tup))
    return reversed_tuple


my_tuple = (1, 2, 3, 4, 5)
result = reverse_tuple(my_tuple)
print("Reversed tuple:", result)





#Sets and its operations. 
#Python program to check if a set is a subset of another set.
def is_subset(set1, set2):
    return set1.issubset(set2)

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
result = is_subset(set1, set2)

if result:
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")







#Dictionaries and its operations. 
#Python program to iterate over dictionaries using for loops.
# Dictionary of student grades
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# Iterating over keys
print("Iterating over keys:")
for key in grades:
    print(key)

# Iterating over values
print("\nIterating over values:")
for value in grades.values():
    print(value)

# Iterating over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in grades.items():
    print(key, "->", value)

    



#computaions using numpy functions
#(a)
import numpy as np

lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(arr)

#(b)
import numpy as np

lst = [1, 2, 3, 4, 5]
tupl = (6, 7, 8, 9, 10)

array_from_list = np.array(lst)
array_from_tuple = np.array(tupl)

print("Array from list:", array_from_list)
print("Array from tuple:", array_from_tuple)

#data manipulations using pandas
#(a)
import numpy as np
import pandas as pd

arr= np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
series_1 = pd.Series([10, 11, 12, 13, 14])

df_from_array = pd.DataFrame(arr, columns=['A', 'B', 'C'])

df_from_series = pd.DataFrame(series_1, columns=['Values'])

print("DataFrame from NumPy array:")
print(df_from_array)

print("DataFrame from Pandas Series:")
print(df_from_series)


#(b)
import pandas as pd

series_1 = pd.Series([10, 20, 30, 40, 50])
series_2 = pd.Series([5, 10, 15, 20, 25])

# Additiom
addition_result = series_1 + series_2

# Subtraction
subtraction_result = series_1 - series_2

# Multiplication
multiplication_result = series_1 * series_2

# Division
division_result = series_1 / series_2

print("Addition Result:")
print(addition_result)

print("Subtraction Result:")
print(subtraction_result)

print("Multiplication Result:")
print(multiplication_result)

print("Division Result:")
print(division_result)


#(c)
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 22, 28, 24],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female'],
    'Salary': [50000, 60000, 45000, 55000, 52000],
    'Department': ['HR', 'IT', 'HR', 'Finance', 'IT']
}


df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("Rows where age is greater than 25:")
filtered_df = df[df['Age'] > 25]
print(filtered_df)

print("Selecting Name and Salary columns:")
selected_columns = df[['Name', 'Salary']]
print(selected_columns)

df['Bonus'] = df['Salary'] * 0.05
print("DataFrame with the Bonus column:")
print(df)

grouped_df = df.groupby('Department')['Salary'].mean()
print("Average salary by department:")
print(grouped_df)

sorted_df = df.sort_values(by='Salary', ascending=False)
print("DataFrame sorted by Salary:")
print(sorted_df)

