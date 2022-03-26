print("File:  " + __file__ + " -   testing")

from lib.matrix import Matrix
mx = Matrix()


mx.load('file_3_test.txt')
mx.pretty_print()

print("END TEST File:  " + __file__)