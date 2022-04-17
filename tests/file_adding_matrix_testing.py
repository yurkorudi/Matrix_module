print("File:  " + __file__ + " -   testing")
from lib.matrix import Matrix 
mx = Matrix()
a = mx.load('./tests/file1-adding.txt', ' ')
mx2 = Matrix()
b = mx2.load('./tests/file2-adding.txt', ' ')
mx.add_matrixes(mx2)



print("END TEST File:  " + __file__)
