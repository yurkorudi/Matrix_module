from matrix import Matrix 
mx = Matrix()
a = mx.load('file_1_test.txt', ' ')
if a:
    print('Loading completed')
else:
    print('Loading failed')