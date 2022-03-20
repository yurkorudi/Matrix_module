from matrix import Matrix
mx = Matrix()


mx.empty_matrix(file_name='emptyyyy1.txt', x_size=3, y_size=3)
mx.load('emptyyyy1.txt')
print(mx.size())