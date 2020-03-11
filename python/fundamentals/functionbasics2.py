# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).


def countdown(num):
    for i in range(num, 0, -1):
        print(i)

# 2. Create a function that will receive a list with two numbers. Print the first value and return the second.


def print_and_return(arr):
    print(arr[0])

    return arr[1]

# 3. Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.


def first_plus_length(arr):
    return arr[0] + len(arr)

# 4. Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False


def greater(arr):
    sub_arr = []
    if len(arr) == 0:
    return False


for x in arr:
    if arr[x] > arr[1]:
    sub_arr.append(arr[x])
print(sub_arr)
print(len(sub_arr))
