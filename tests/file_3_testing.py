print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix
mx = Matrix()
a = mx.load('./tests/file_3_test.txt', ' ')
if a:
    print("LOADING COMPLETED")
    b = mx.pretty_print()
    if b:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
else:
    print("LOADING FAILED")
    print("TEST FAILED")

print("END TEST File:  " + __file__)
    