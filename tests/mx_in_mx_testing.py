print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/for_mx_in_mx_test_0.txt', ' ')
mx2 = Matrix()
mx2.load('./tests/for_mx_in_mx_test_1.txt', ' ')
a = mx.mx_in_mx(mx2)
print(a)

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/for_mx_in_mx_test_2.txt', ' ')
mx2 = Matrix()
mx2.load('./tests/for_mx_in_mx_test_3.txt', ' ')
a = mx.mx_in_mx(mx2)
print(a)

from lib.matrix import Matrix 
mx = Matrix()
mx.load('./tests/for_mx_in_mx_test_4.txt', ' ')
mx2 = Matrix()
mx2.load('./tests/for_mx_in_mx_test_5.txt', ' ')
a = mx.mx_in_mx(mx2)
print(a)

















print("END TEST File:  " + __file__)