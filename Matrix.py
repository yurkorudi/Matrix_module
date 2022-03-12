import math
from new_matrix import New_matrix
from os import path



class Matrix:
    def __init__(self):
        self.mx = []

    def load(self, file_name, separator=' '):
        self.file_to_read = file_name
        self.separator = separator
        if not path.exists(self.file_to_read):
            print('Wrong file name, file doesnt exist')
            return False
        else:
            lines = []
            self.mx_list = []
            with open(self.file_to_read, 'r') as file:
                lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                self.mx_list.append(line.split(self.separator))
            for i in range(len(self.mx_list)):
                while('' in self.mx_list[i]):
                    self.mx_list[i].remove('')  
            for i in range(len(self.mx_list)):
                try:
                    if len(self.mx_list[i]) != len(self.mx_list[i+1]):
                        print('''File you loaded isn't matrix, chek all columns and rows should be same''')
                        return False
                except IndexError:
                    pass
            print('Here is your matrix: ',  self.mx_list)
            file.close()
            return False

    def write(self):
        a = New_matrix()
        a.write_new_mx(self)
        return False

    def size(self):
        lenght = len(self.mx_list[0])
        height = len(self.mx_list)
        print("Size: ", lenght, 'x', height)
        answer = (lenght, height)
        return answer

    def is_digital(self, file_name, separator=' '):
        self.load(file_name, separator)
        a = self.mx_list
        self.int_t = 0
        self.str_t = 0
        for i in range(len(a)):
            for b in range(len(a[i])):
                try:
                    if int(a[i][b]):
                        self.int_t += 1
                except ValueError:
                    self.str_t += 1
        
        if self.int_t > 0 and self.str_t > 0:
            print("You have non-digital matrix")
        elif self.str_t == 0 and self.int_t >= 0:
            print("You have digital matrix")
        return False

    def save(self, file_name, mx):
        matrix_to_save = mx
        with open(file_name, 'w') as file:
            for i in range(len(matrix_to_save)):
                for a in range(len(matrix_to_save[i])):
                    file.write(matrix_to_save[i][a])
                    file.write(' ')
                file.write('\n')
        file.close()
        return False




