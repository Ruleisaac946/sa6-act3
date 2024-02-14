sum_of_digits = lambda n: sum(int(digit) for digit in str(n))

number = 12345

result = sum_of_digits(number)

print("Sum of digits of", number, "is:", result)
