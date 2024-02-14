def exponential_mapping(numbers, n):

    result = list(map(lambda x: x ** n, numbers))
    return result


numbers = [1, 2, 3, 4, 5]
n = 2

result = exponential_mapping(numbers, n)
print("Result:", result)
