print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file1-adding.txt', ' ')
mx2 = Matrix()
b = mx2.load('./tests/file2-adding.txt', ' ')
a = mx.add_matrixes(mx2)
print(mx.mx_list)
if not a:
    print('Test - FAILED')
else:
    print('Test - PASSED')

mx = Matrix()
a = mx.load('./tests/file1-adding_int.txt', ' ')
mx2 = Matrix()
b = mx2.load('./tests/file2-adding_ints.txt', ' ')
a = mx.add_matrixes(mx2)
print(mx.mx_list)
if not a:
    print('Test - FAILED')
else:
    print('Test - PASSED')

print("END TEST File:  " + __file__)
