'''
### Dictionaries (similar to JS objects):

### Declaring a Dictionary:

phonebook = {}
phonebook['Joshua'] = 1234098239
phonebook['Austen'] = 1234098237
phonebook['Elizabeth'] = 1234098233

print(phonebook)

phonebook = {
  "Joshua": 1234098239,
  "Austen": 1234098237,
  "Elizabeth": 1234098233
}

phonebook["Parth"] = 1234098231

print(phonebook)

### Iterating through a Dictionary:

for name, number in phonebook.items():
  print("Name: %s, Phone Number: %d" % (name, number))

### Removing items from a Dictionary:

del. method (no return):
del phonebook["Parth"]
print(phonebook)

pop method (returns deleted value):
print(phonebook.pop("Elizabeth"))
print(phonebook)
'''

# ===================================================================

"""
Add "Herb" to the phonebook with the number 7653420789.
Remove "Bill" from the phonebook.
"""
phonebook = {
    "Abe": 4569874321,
    "Bill": 7659803241,
    "Barry": 6573214789
}

# YOUR CODE HERE
phonebook["Herb"] = 7653420789
del phonebook["Bill"]

print('YOU-DO #1:')
print('==============================================================')
# Should print Herb is in the phonebook.
if "Herb" in phonebook:
    print("Herb is in the phonebook.")

# Should print Bill is not in the phonebook.
if "Bill" not in phonebook:
    print("Bill is not in the phonebook.")

# ===================================================================

'''
### Mutable/Immutable Objects:

### Mutable Object Types (can be changed):

  - Lists
  - Dictionaries
  - Sets
  - User defined classes

### Immutable Object Types (cannot be changed):

  - Integers
  - Floating point numbers
  - Decimals
  - Booleans
  - Strings
  - Tuples
  - Ranges

my_list = [1, 2, 3]
print(my_list)

my_list[1] = 7
print(my_list)


my_tuple = (1, 2, 3)
print(my_tuple)

# my_tuple[1] = 7
# print(my_tuple)
# Will throw an error

# id(): tells the identity of an object in python
print(id(my_tuple))
print(id(my_list))

my_string = "Hello"
print(my_string)

# my_string[1] = "y"
# Will throw an error
'''
print('==============================================================')
print('YOU-DO #2:')
print('==============================================================')

"""
Use built-in Python methods to print the identity, type, and value of `example_object`.
"""
example_object = "I have an identity, type, and value."
print(id(example_object))
print(type(example_object))
print(example_object)


"""
Use a built-in Python operator to determine if `a` and `b` have the same identity.
"""
a = 1
b = a
print(id(a) == id(b))
# ===================================================================
'''
### Time Complexity / Big O Notation:

## Algorithm: Set of instructions for accomplishing a task

## Time:

## Big O Notation: Language we use for describing how efficient an algorithm is

## Common Runtimes:

  - Constant O(1): Runtime is unaffected by input size - Ideal solution
  - Logarithmic O(log n): As the input size increases, runtime grows slightly slower -     Good solution
  - Linear O(n): As the input size increases, runtime grows at the same rate - Good        solution
  - Polinomial O(n^c): As the input size increases, runtime grows at faster rate - May     work for small inputs, but not scalable
  - Exponential O(c^n): As input size increases, runtime grows at a much faster rate -     Inefficient
  - Factorial O(n!): As the input size grows, runtime will grow astronomically, even       with relatively small inputs - Exceptionally inefficient

=============================

def print_one_item(items):
  print(items[0]) # O(1) - Constant

=============================  

def print_every_item(items):
  for item in items:
    print(item) # O(n) - Linear

=============================

def print_pairs(items):
  for item_one in items:
    for item_two in items:
      print(item_one, item_two) # O(n^2) - Quadratic

=============================

def do_a_bunch_of_stuff(items): # O(1 + n/2 + 2000)
  last_idx = len(items) - 1
  print(items[last_idx]) # O(1)

  middle_idx = len(items) / 2
  idx = 0
  while idx < middle_idx: # O(n/2)
    print(items[idx])
    idx = idx + 1

  for num in range(2000): # O(2000)
    print(num) # O(n) - Linear

=============================

def do_different_things(item): # O(n + n^2)
  for item in items: # O(n)
    print(item)

  for item_one in items: # O(n * n) = O(n^2)
    for item_two in items:
      print(item_one, item_two) # O(n^2) - Quadratic

=============================

def search_for_thing(items, thing):
  for item in items:
    if item == thing:
      return True

  return False # O(n) - Linear

=============================

# our turn
def foo(n):
  i = 1
  while i < n:
    print(i)
    i *= 2 # O(log n) - Logarithmic

=============================
'''
print('==============================================================')
print('YOU-DO #3:')
print('==============================================================')
"""
Classify the runtime complexity of the number_of_steps function below using Big O notation.
"""
def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1
        steps = steps + 1
    return steps

print('O(n)')


"""
Classify the runtime complexity of the sorted_squares function below using Big O notation.
"""
def sorted_squares(A):
    N = len(A)
    j = 0
    while j < N and A[j] < 0:
        j += 1
    i = j - 1

    ans = []
    while 0 <= i and j < N:
        if A[i]**2 < A[j]**2:
            ans.append(A[i]**2)
            i -= 1
        else:
            ans.append(A[j]**2)
            j += 1

    while i >= 0:
        ans.append(A[i]**2)
        i -= 1
    while j < N:
        ans.append(A[j]**2)
        j += 1

    return ans

print('O(n^2)')

"""
Classify the runtime complexity of the insertion_sort function below using Big O notation.
"""
def insertion_sort(arr):
    for i in range(1, len(arr)): 
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]: 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key

print('O(n)')

# =============================
'''
### Space Complexity: Efficiency of memory usage instead of the number of operations

def print_lambda_n_times(n):
  for i in range(n):
    print("lambda") # O(1) - Constant

=============================

def append_to_list_n_times(n):
  my_list = []

  for _ in range(n):
    my_list.append("lambda")

  return my_list # O(n) - Linear

=============================

def get_the_max(items_list):
  maximum = float("-inf")
  for item in items_list:
    if item > maximum:
      maximum = item

  return maximum # O(1) - Constant

=============================
'''
print('==============================================================')
print('YOU-DO #4:')
print('==============================================================')

"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i-2] + lst[i-1])
    
    return lst[n-1] # O(n)



"""
Use Big O notation to classify the space complexity of the function below.
"""
def fibonacci_two(n):
    x, y, z = 0, 1, None
    
    if n == 0:
        return x
    if n == 1:
        return y
    
    for i in range(2, n):
        z = x + y
        x, y = y, z

    return z # O(n)



"""
Use Big O notation to classify the space complexity of the function below.
"""
def do_something(n):
    lst = []
    for i in range(n):
        for j in range(n):
            lst.append(i + j)
    
    return lst # O(n)

# =============================
'''
### List Comprehensions

 - Iterating
 - Mapping
 - Filtering

# Words

sentence = "Every moment is a fresh beginning."
words = sentence.split()
word_lengths = [len(word) for word in words]

# for word in words:
#   word_lengths.append(len(word))

# print(word_lengths)

# =============================

# Numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]

# for number in numbers:
#   if number % 2 == 0:
#     even_numbers.append(number)

print(even_numbers)

# even_numbers_lst_comp = []
'''

# =============================

"""
Use a list comprehension to create a new list called new_list out of the numbers list. Use the list comprehension to make sure that the new_list only contains positive numbers and make sure they are cast as integers into the new_list.
"""

numbers = [22.3, -184.4, 57.8, 99.6, -18.2, 84.2, 71.3]

new_list = [int(number) for number in numbers if number > 0]
print(new_list)