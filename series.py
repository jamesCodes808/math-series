import math
# create function named fibonacci
# function should have one parameter n
# function should return the nth value in the fibonacci series
# can be implemented using recursion or iteration

# The Fibonacci Series is a numeric series starting with the integers 0 and 1.
# In this series, the next integer is determined by summing the previous two. This gives us:
# 0, 1, 1, 2, 3, 5, 8, 13, ...


# When asking for the nth number in series presume starting at zero:
# fibonacci(0) == 0, fibonacci(1) == 1, fibonacci(2) == 1, etc.

def fibonacci(n):
    """
    - Takes in a parameter, that parameter represents the nth number of the fibonacci sequence
    - First 2 numbers in the sequence will always be 0 and 1
    - Finds that number with the formula:
    F(n) = F(n-1) + F(n-2)
    ex: fibonacci(4) = fibonacci(4-1) + fibonacci(4-2) = 3
    :return:
    return 0 if n <= 0 else return 1 if n <= 1 else return fibonacci(n-1) + fibonacci(n-2)
    """

    if n <= 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



# create function named lucas
# takes in one parameter n
# returns the nth value in lucas numbers
# can be implemented using recursion or iteration

# The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1.
# The resulting series looks like this:
# 2, 1, 3, 4, 7, 11, 18, 29, ...

def lucas(n):
    """
    - Takes in a parameter, that parameter represents the nth number of the lucas number sequence
    - First 2 numbers in the sequence will always be 2 and 1
    - Finds that number with the formula:
    L(n) = L(n-1) + L(n-2)
    ex: lucas(4) = lucas(4-1) + lucas(4-2) = 7
    :return:
    return 2 if n <= 0 else return 1 if n <= 1 else return lucas(n-1) + lucas(n-2)
    """

    if n <= 0:
        return 2
    elif n <= 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

# create function named sum_series
# takes 1 required parameter, 2 optional parameters
# required parameter determines which element in the series to print
# 2 optional parameters will have default values of 0 and 1, determines the first 2 values for the series to be produced
# Calling this function with no optional parameters will produce numbers from the fibonacci series
# calling with 2 optional args and 1 req arg, produces values from lucas numbers
# Other values for optional args will produce other series

def sum_series(n, n2=0, n3=1):
    """
    - Takes in a required parameter and two optional parameters that have default values (n, n2=0, n3=1)
    |
    - When required argument is provided, returns nth number in fibonacci sequence using formula F(n) = F(n-1) + F(n-2)
    |
    - When required argument is provided, and optional parameters are 2 and 1, provides lucas numbers using formula L(n) = L(n-1) + L(n-2)
    |
    - When required argument is provided and optional parameters are not 0 and 1 or 2 and 1, provides list of juggler sequence numbers, if n is even, divides by 2, if n is odd, multiply by 3 and add 1 until n == 1
    :param n: required, int value
    :param n2: optional, default value of 0
    :param n3: optional, default value of 1
    :return:
    fibonacci(n-1) + fibonacci(n-2) if (n)
    |
    lucas(n-1) + lucas(n-2) if (n and n2 == 2 and n3 == 1)
    |
    while n !=1
    n = n ** 0.5 if even
    n = n ** 1.5 if odd
    [n]
    """
    if n2 == 0 and n3 == 1:
        return 0 if (n <= 0) else 1 if (n <= 1) else fibonacci(n - 1) + fibonacci(n - 2)

    if n2 == 2 and n3 == 1:
        return 2 if (n <= 0) else 1 if (n <= 1) else lucas(n - 1) + lucas(n - 2)

    if n2 != 0 or n3 != 1 and n2 != 2 or n3 != 1:
        sequence = [n]
        while n != 1:
            if n%2 == 0:
                n = int(n ** 0.5)
            else:
                n = int(n ** 1.5)
            sequence.append(n)
        return sequence
# call stack
