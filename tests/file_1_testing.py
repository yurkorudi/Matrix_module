print("File:  " + __file__ + " -   testing")


# import sys
# import os
# sys.path.insert(0, os.path.dirname(sys.path[0]))

from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file_1_test.txt', ' ')
if a:
    print('Loading completed')
    print('TEST - PASSED')
else:
    print('Loading failed')
    print('TEST - FAILED')


print("END TEST File:  " + __file__)