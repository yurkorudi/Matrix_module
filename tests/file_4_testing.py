print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix
import random
mx = Matrix()
for i in range(4):
    mx.mx_list.append([])
    for a in range(3):
        mx.mx_list[i].append(random.randint(0,9))
a = mx.save("./tests/file0.txt")
a = mx.save("./tests/file1.txt", " ")
a = mx.save("./tests/file2.txt", ",")
if a:
    print("Saving copleted")
    print("TEST PASSED")
else:
    print("TEST FAILED")
print("END TEST File:  " + __file__)