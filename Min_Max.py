numbers = [100,300,232,1222,5667,145]
max_num = numbers[0]
min_num = numbers[0]
for number in numbers:
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
print("Maximum number in the sequence:", max_num)
print("Minimum number in the sequence:", min_num)
