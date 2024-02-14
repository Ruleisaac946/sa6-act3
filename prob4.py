def intersection(list1, list2):

    intersection_list = list(filter(lambda x: x in list1, list2))
    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = intersection(list1, list2)
print("Intersection:", result)
