# 5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1
from collections import Counter
# {5: 3, 4: 6, 3: 3, 2: 1}, 4
def numbers_statistics(numbers: list[int]) -> tuple[dict, int]:
    numbers_statistics_dict = dict()
    for number in numbers:
        if number in numbers_statistics_dict:
            numbers_statistics_dict[number] += 1
        else:
            numbers_statistics_dict[number] = 1
    # max_number = float('-inf') # float('inf')
    # max_count = float('-inf')
    max_number = -1
    max_count = 0
    for number, count in numbers_statistics_dict.items():
        if count > max_count:
            max_count = count
            max_number = number

    return numbers_statistics_dict, max_number

def numbers_statistics_counter(numbers: list[int]) -> tuple[dict, int]:
    counter = Counter(numbers)
    return dict(counter), counter.most_common(1)[0][0]

numbers = [5, 0, 5, 3, 7, 3, 8, 7, 1, 4, 1, 0, 3, 5, 3, 5, 6, 0, 7, 9, 0, 8, 9, 4, 2, 3, 3, 2, 7, 1]
print(numbers_statistics(numbers))

print(numbers_statistics_counter(numbers))
