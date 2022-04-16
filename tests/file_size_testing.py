print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix
mx = Matrix()
mx.load('./tests/file_size_test.txt', ' ')
a = mx.size()
if not a:
    print("SIZE FUNTCION RETURNED ERROR")
    print("TEST FAILED")
else:
    print(a)
    print("TEST COMPLITED")
print("END TEST File:  " + __file__)

