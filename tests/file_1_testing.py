import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]))

from matrix import Matrix 
mx = Matrix()
a = mx.load('file_1_test.txt', ' ')
if a:
    print('Loading completed')
else:
    print('Loading failed')