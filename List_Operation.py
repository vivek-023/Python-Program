# Find Product of List
lst = [15,20,54,32,12]
product = 1
for item in lst:
    product *= item
print("Product of all items in the list:", product)

# Find the smallest number in a list
smallest = lst[0]
for item in lst:
    if item < smallest:
        smallest = item
print("Smallest number in the list:", smallest)

# Find the largest number in a list
largest = lst[0]
for item in lst:
    if item > largest:
        largest = item
print("Largest number in the list:", largest)
# Reversing the list
reversed_list = []
for i in range(len(lst) - 1, -1, -1):
    reversed_list.append(lst[i])
print("Reversed list:", reversed_list)
