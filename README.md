
# Built-in Python Operators, Functions and Methods - Lab

## Introduction
We've looked at some of the built-in methods, functions, and the operators that Python provides us with. These are all very powerful tools we can (and will) use in our code. Below, we'll put these new tools to use to solve the tests in this lab.

## Objectives
You will be able to:
* Use base Python methods like `.append()`, `.upper()` and `.capitalize()`
* Understand (simply) and explain what built in Python methods are
* Understand, explain and use some base Python functions like `len()`, `type()`, `sum()`, `max()` and `min()`
* Understand and explain what functions are and why they’re useful
* Understand, explain and use Python comparison, logical, and identity operators

## Instructions

Let's start out by using some built-in functions and methods. Employ the appropriate functions and methods to get the intended result.


```python
yell_hello = "hello, there" # "HELLO, THERE"
yell_hello.upper()
```




    'HELLO, THERE'




```python
whisper_hey = "PSST, HEY" # "psst, hey"
whisper_hey.lower()
```




    'psst, hey'




```python
flatiorn_mantra = "LEARN. LOVE. CODE." # "Learn. Love. Code"
flatiorn_mantra.title()
```




    'Learn. Love. Code.'




```python
type_string = "i'm a string" # str
type(type_string)
```




    str




```python
type_list = ["i'm", "a", "list"] # list
type(type_list)
```




    list




```python
lenght_of_list = ["i'm", "a", "list"] # 3
len(lenght_of_list)
```




    3




```python
longest_word_in_list = ["i'm", "a", "list"] # "list"
max(longest_word_in_list)
```




    'list'




```python
smallest_number = [1, 3, 4, 78] # 1
smallest_number[0]
```




    1




```python
sum_of_numbers = [1,2,3,5] # 11
sum(sum_of_numbers)
```




    11



Uncomment out the code in each cell as you start working on them. For example, when you begin on the first two examples in cell one, remove the first `#` on each line. Then, use the correct comparison operator to get the desired output, which you will find in a second comment at the end of the line feel free to remove this comment as well or keep it. Finally, Replace the `[COMPARISON]`, with the correct operator. See the example below.

```python
# boolean_compare = False [COMPARISON] True # True 
=> boolean_compare = False != True # True
OR
=> boolean_compare = False != True
```

Once uncommented, you can run the tests to see if your comparisons are working the way we would like them to be.

> **Remember** the comparison operators are: `==`, `!=`, `<`, `>`, `<=`, `>=`


```python
boolean_compare = True != True # False
print(boolean_compare)
boolean_compare2 = False == True # False
boolean_compare2
```

    False





    False




```python
number_compare = 10 == 10 # True
print(number_compare)
number_compare2 = -20 < 30 # True
print(number_compare2)
number_compare3 = 4 > 5 # False
print(number_compare3)
```

    True
    True
    False



```python
string_compare = "stacy" == "STACY".lower() # True
print(string_compare)
string_compare2 = "hey i love python!" == "hi love python" # False
print(string_compare2)
string_compare3 = "this string is bigger than the other" > "that is true" # True
print(string_compare3)
```

    True
    False
    True


In the next section, do not use either `==` or `!=` operators


```python
list_compare = len([0,0,0,0]) > len([0,0,0]) # True
print(list_compare)
list_compare2 = [1,0,0] >= [0,0,0] # True
print(list_compare2)
list_compare3 = [0,0,0] >= [0,0,3] # False
print(list_compare3)
list_compare4 = [0,0,3,0] > [0,0,3] # True
print(list_compare4)
list_compare5 = [0,0,4,0] < [0,0,3] # False
print(list_compare5)
```

    True
    True
    False
    True
    False


### Practicing Identity and Logical Operators

In this next section, use the identity and logical operators to get the desired output as you did in the examples above using the comparison operators.

> **Remember:**
the **logcial operators** are: `and`, `or`, & `not` and
the **identity operators** are: `is` & `is not`

Use logical opertors for this section


```python
logical_compare = 2 and [] # []
print(logical_compare)
logical_compare2 = not [] # True
print(logical_compare2)
logical_compare3 = 0 and [] # 0
print(logical_compare3)
logical_compare4 = True and 2 # 2
print(logical_compare4)
logical_compare5 = 2 or 3 # 2
print(logical_compare5)
logical_compare6 = not True # False
print(logical_compare6)
logical_compare7 = False and 2 # False
print(logical_compare7)
```

    []
    True
    0
    2
    2
    False
    False


Use identity opertors for this section


```python
a = []
b = a
identity_compare = {} is {} # False
print(identity_compare)
identity_compare2 = a is b # True
print(identity_compare2)
identity_compare3 = b is not [] # True
print(identity_compare3)
identity_compare4 = 9 is not 10 # True
print(identity_compare4)
identity_compare5 = "Same" is not "Same" # False
print(identity_compare5)
identity_compare6 = [1,3,4] is [1,2,3] # False
print(identity_compare6)
```

    False
    True
    True
    True
    False
    False


# Summary
Great work! After all that, there's nothing we can't compare, well I guess apples and oranges might still off the table. We practiced using comparison, logical, and identity operators in Python to compare elements of the same and different datatypes and or values. Going forward, there will be plenty of instances where we will need to compare elements. So, it is important to have a good understanding of how each of these operators works. Don't worry, as with all concepts in programming, the more we work with something the better we understand it. 
