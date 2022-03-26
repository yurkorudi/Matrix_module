print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file_2_test.txt', ' ')
if a:
    print('LOADING COMPLETED')
    a = mx.is_digital()
    if a:
        print("You have digital matrix")
    else:
        print('You have non-digital matrix')
    print('TEST - PASSED')
else:

    print('LOADING FAILED')

print("END TEST File:  " + __file__)
