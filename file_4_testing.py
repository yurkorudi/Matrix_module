from matrix import Matrix
m = Matrix()

# заповнити матрицю випадковими значеннями розмірв 3х4
m.load('file3.txt', ', ')
#вззяв уже готову 
m.save("file0.txt")
m.save("file1.txt", " ")
m.save("file2.txt", ",")