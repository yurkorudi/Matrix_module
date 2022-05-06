print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/file_size_test.txt', ' ')
mx.pretty_print()
print("____________")
if mx.divis_to_all(2):
    mx.pretty_print()
    print("TEST - Passed")
else:
    print("TEST - Failed")
    
print("END TEST File:  " + __file__)