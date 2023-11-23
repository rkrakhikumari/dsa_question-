from array import *

# given an array with some integer type values. write a python script to sort array values
my_array = array('i', [1,2,3,4,5,9,8,6,8,10])
sorted_array = array('i', sorted(my_array))
print(my_array)
print(sorted_array)


# given a list of heterogenous elements write a python script to remove all the non int values from the list
my_list = [1,'apple', 2,'seven', 78, 'banana']
filtered_list = [x for x in my_list if isinstance(x,int)]
print(my_list)
print(filtered_list)


# write a python script to calculate average of elements of a list
my_list = [1,2,3,4,5,6,7,8,9]
average = sum(my_list)/ len(my_list)
print(average)


# write a python script to create a list of first N prime numbers
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes
n = 5
prime_numbers = generate_primes(n)
print(f"The first {n} prime number are: {prime_numbers}")


# write a python script to create a list of first N terms of a fabonacci series

def generate_fibonacci(n):
    fibonacci_series = []

    a,b = 0, 1
    for _ in range(n):
        fibonacci_series.append(a)
        a,b = b, a+b
    return fibonacci_series
n =8
fibonacci_terms = generate_fibonacci(n)
print(f"the first {n} terms of the fibonacci series are: {fibonacci_terms}")




