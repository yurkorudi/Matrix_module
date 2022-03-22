import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]))


from matrix import Matrix 
mx = Matrix()
a = mx.load('file_2_test.txt', ' ')
if a:
    print('Loading completed')
else:
    print('Loading failed')
a = mx.is_digital()
if a:
    print("You have digital matrix")
else:
    print('You have non-digital matrix')