print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/file_comparing_1.txt', ' ')
mx.pretty_print()
print("____________")
mx2 = Matrix()
mx2.load('./tests/file_comparing_2.txt', ' ')
mx2.pretty_print()

a = mx.matrix_comparing(mx2)

print("TEST - Passed")

    
print("END TEST File:  " + __file__)