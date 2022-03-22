import sys
import os
sys.path.insert(0, os.path.dirname(sys.path[0]))

from matrix import Matrix
mx = Matrix()
mx.load('file1.txt', ' ')
mx.pretty_print()