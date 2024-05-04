
# 5! = 5 * 4 * 3 * 2 * 1

def factorial(n: int) -> int:
    # Stopping block
    if n == 1:
        return 1
    # Recursive block
    return n * factorial(n - 1)

def factorial_explained(n: int, level=0) -> int:
    if n == 1:
        print(f'Level {level}: factorial({n}) = 1')
        return 1
    print(f'Level {level}: factorial({n}) = {n} * factorial({n - 1})')
    result = n * factorial_explained(n - 1, level=level + 1)
    print(f'Level {level}: factorial({n}) = {result}')
    return result

# print(factorial_explained(5))

# print(factorial_explained(1000))
# Tail recursion 
# def factorial_tail(n: int, accumulator=1) -> int:
#     # Stopping block
#     if n == 1:
#         return accumulator
#     # Recursive block
#     return factorial_tail(n - 1, n * accumulator)

def factorial_tail(n: int, accumulator=1, level=0) -> int:
    # Stopping block
    if n == 1:
        print(f'Level {level}: factorial({n}) = 1 | accumulator = {accumulator}')
        return accumulator
    # Recursive block
    print(f'Level {level}: factorial({n}) = factorial_tail({n - 1}, {n} * {accumulator}) | accumulator = {accumulator}')
    result = factorial_tail(n - 1, n * accumulator, level=level + 1)
    print(f'Level {level}: factorial({n}) = {result} | accumulator = {accumulator}')
    return result

print(factorial_tail(5))
