print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file_1_test.txt', ' ')
if a:
    print('Loading completed')
    print('TEST - FAILED')
else:
    print('Loading failed')
    print('TEST - PASSED')


print("END TEST File:  " + __file__)