print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/file_2_test.txt', ' ')
a = mx.get_value_by_coords(0,0)
if a:
    print("Test - PASSED")
    print(a)
else: 
    print("Test - FAILED")



print("END TEST File:  " + __file__)