from matrix import Matrix
mx = Matrix()


mx.empty_matrix(file_name='empty1.txt', x_size=3, y_size=3)

print(mx.load('lala.txt'))
print(mx.size())