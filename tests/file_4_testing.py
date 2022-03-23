import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]))

from matrix import Matrix
import random
m = Matrix()


for i in range(4):
    m.mx_list.append([])
    for a in range(3):
        m.mx_list[i].append(random.randint(0,9))


m.save("file0.txt")
m.save("file1.txt", " ")
m.save("file2.txt", ",")
print("Done")