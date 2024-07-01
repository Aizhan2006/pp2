#1 Create a generator that generates the squares of numbers up to some number N.
def generate_squares(N):
    for i in range(N + 1):
        yield i * i

# Example usage:
N = 10
squares_generator = generate_squares(N)
for square in squares_generator:
    print(square)


#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

# Example usage:
n = 20
even_numbers_generator = even_numbers(n)
print(", ".join(str(num) for num in even_numbers_generator))


#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Example usage:
n = 36
divisible_generator = divisible_by_3_and_4(n)
for num in divisible_generator:
    print(num)


#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Example usage:
a = 1
b = 5
for square in squares(a, b):
    print(square)


#5 Implement a generator that returns all numbers from (n) down to 0.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

# Example usage:
n = 10
for num in countdown(n):
    print(num)
