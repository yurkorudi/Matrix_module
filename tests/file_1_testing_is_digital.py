print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/file1_digital.txt', ' ')

if mx.is_digital():
    print('TEST - PASSED')
    
else:
    print('TEST - FAILED - Matrix should be digital')
    


print("END TEST File:  " + __file__)