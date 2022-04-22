print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/file_2_test.txt', ' ')
a = mx.add_value_by_coords(1,1,9)
if a:
    print("Test - PASSED")
    mx.pretty_print()
else: 
    print("Test - FAILED")



print("END TEST File:  " + __file__)