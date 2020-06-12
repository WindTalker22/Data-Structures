arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cache = {}


# for num_1 in arr_1:
#     for num_2 in arr_2:
#         if num_1 == num_2:
#             print(num_2)

for num_1 in arr_1:
    cache[num_1] = True

    for num_2 in arr_2:
        if num_2 in cache:
            print(True)
