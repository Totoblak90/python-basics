with open("file1.txt") as f1:
    file1_list = f1.readlines()
    list_1 = [int(n.strip()) for n in file1_list]

with open("file2.txt") as f2:
    file2_list = f2.readlines()
    list_2 = [int(n.strip()) for n in file2_list]

result = [n for n in list_1 if n in list_2]

print(result)