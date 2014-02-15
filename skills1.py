# Things you should be able to do.

# Write a function that takes a list and returns a new list with only the odd numbers.
def all_odd(some_list):
    new_list = []
    for i in some_list:
        if i % 2 == 1:
            new_list.append(i)
        else:
            pass
    return new_list

# Write a function that takes a list and returns a new list with only the even numbers.
def all_even(some_list):
    new_list = []
    for i in some_list:
        if i % 2 == 0:
            new_list.append(i)
        else:
            pass
    return new_list

# Write a function that takes a list of strings and a new list with all strings of length 4 or greater.
def long_words(word_list):
    new_list = []
    for i in word_list:
        if len(i) >= 4:
            new_list.append(i)
        else:
            pass
    return new_list

# Write a function that finds the smallest element in a list of integers and returns it.
def smallest(some_list):
    return None

# Write a function that finds the largest element in a list of integers and returns it.
def largest(some_list):
    return None

# Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.
def halvesies(some_list):
    new_list = []
    for i in some_list:
        new_list.append(i/2)
    return new_list

# Write a function that takes a list of words and returns a list of all the lengths of those words.
def word_lenths(word_list):
    lengths = []
    for i in word_list:
        lengths.append(len(i))
    return lengths

# Write a function (using iteration) that sums all the numbers in a list.
def sum_numbers(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

# Write a function that multiplies all the numbers in a list together.
def mult_numbers(numbers):
    total = 1
    for i in numbers:
        total = total * i
    return total

# Write a function that joins all the strings in a list together (without using the join method) and returns a single string.
def join_strings(string_list):
    joined = ""
    for i in string_list:
        joined += i + " "
    return joined

# Write a function that takes a list of integers and returns the average (without using the avg method)
def average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total/len(numbers)

words = ["dog", "cat", "motorcycle", "something","none"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
