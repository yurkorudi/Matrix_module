print("File:  " + __file__ + " -   testing")

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