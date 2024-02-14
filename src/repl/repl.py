my_list = ["A", "B", "C"]

for i in enumerate(my_list):
    print(i)

# Enumerate from index 2 to index 3 (exclusive)
for index, item in enumerate(my_list[1:3], start=1):
    print(index, item)
