# Subtracking
from lib.matrix import Matrix
mx1 = Matrix()
mx1.load('./tests/file_size_test.txt', ' ')
mx1.subtrack_to_all(2)
mx2 = Matrix()
mx2.load('./tests/file_size_test.txt', ' ')
for i in range(len(mx2.mx_list)):
    for a in range(len(mx2.mx_list[i])):
        mx2.mx_list[i][a] = mx2.mx_list[i][a] - 2

if mx1.mx_list == mx2.mx_list:
    print('TEST - PASSED')
    print(mx1.mx_list)
else:
    print('TEST - FAILED')

mx1.multiply_to_all(3)

for i in range(len(mx2.mx_list)):
    for a in range(len(mx2.mx_list[i])):
        mx2.mx_list[i][a] = mx2.mx_list[i][a] * 3

if mx1.mx_list == mx2.mx_list:
    print('TEST - PASSED')
    print(mx1.mx_list)
else:
    print('TEST - FAILED')

mx1.divis_to_all(5)

for i in range(len(mx2.mx_list)):
    for a in range(len(mx2.mx_list[i])):
        mx2.mx_list[i][a] = mx2.mx_list[i][a] / 5

if mx1.mx_list == mx2.mx_list:
    print('TEST - PASSED')
    print(mx1.mx_list)
else:
    print('TEST - FAILED')

