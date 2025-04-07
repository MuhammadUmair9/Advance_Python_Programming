my_list = []
for m in range(1, 11):
    number =int(input(f"Enter the {m} Number:"))
    my_list.append(number)
my_list.sort()
print("Max:", max(my_list))
print("Min:", min(my_list))
print("Sort:", my_list)
