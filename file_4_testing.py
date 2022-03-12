from matrix import Matrix
import random
m = Matrix()
matrixx_list = []

for i in range(4):
    matrixx_list.append([])
    for a in range(3):
        matrixx_list[i].append(random.randint(0,9))


m.save("file0.txt", matrixx_list)
m.save("file1.txt", matrixx_list, " ")
m.save("file2.txt", matrixx_list, ",")
print("Done")