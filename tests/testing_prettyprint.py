print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix
mx = Matrix()
a = mx.load('./tests/file_prettyprint_test.txt', ' ')
if a:
    print("Loading completed")
    b = mx.pretty_print()
    if b:
        print("TEST PASSED")
    else:
        print("TEST FAILED")
else:
    print("TEST FAILED")
print("END TEST File:  " + __file__)