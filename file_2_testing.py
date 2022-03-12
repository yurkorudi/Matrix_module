from matrix import Matrix 
mx = Matrix()
mx.load('file_2_test.txt', ' ')
a = mx.is_digital()
if a:
    print("You have digital matrix")