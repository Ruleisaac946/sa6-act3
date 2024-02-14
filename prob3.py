def find_maximum(numbers, compare):
    maximum = numbers[0]

    for num in numbers[1:]:
        maximum = compare(maximum, num)

    return maximum

numbers = [5, 10, 3, 8, 2]

compare_function = lambda x, y: x if x > y else y

maximum_number = find_maximum(numbers, compare_function)
print("Maximum number:", maximum_number)