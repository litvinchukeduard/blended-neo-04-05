from typing import Generator, Any
# [YieldType, SendType, ReturnType]
#  yield        send()     return     
# def generate_even_numbers(min: int, max: int) -> Generator[int, None, None]:
def generate_even_numbers(min: int, max: int) -> Generator[int, None, None]:
    for number in range(min, max):
        if number % 2 == 0:
            yield number


# def basic_generator():
#     result = yield "Hello"
#     print(result)
#     yield 4

# my_generator = basic_generator()
# my_generator.send("Hello")

my_even_number_generator = generate_even_numbers(1, 10)
# try:
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
#     print(next(my_even_number_generator))
# except StopIteration:
#     print("iteration stopped")

for even_number in my_even_number_generator:
    print(even_number)

