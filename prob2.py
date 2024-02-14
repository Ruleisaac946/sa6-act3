strings = ["banana", "apple", "orange", "grape", "kiwi", "pear"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted strings:", sorted_strings)
