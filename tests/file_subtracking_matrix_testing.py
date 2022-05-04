print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file1-subtracking.txt', ' ')
mx2 = Matrix()
b = mx2.load('./tests/file2-subtracking.txt', ' ')
a = mx.subtrack_matrixes(mx2)
mx.pretty_print()
if not a:
    print('Test - FAILED')
else:
    print('Test - PASSED')

mx = Matrix()
a = mx.load('./tests/file1-subtracking_int.txt', ' ')
mx2 = Matrix()
b = mx2.load('./tests/file2-subtracking_int.txt', ' ')
a = mx.subtrack_matrixes(mx2)
mx.pretty_print()
if not a:
    print('Test - FAILED')
else:
    print('Test - PASSED')

print("END TEST File:  " + __file__)