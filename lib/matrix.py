import os

class Matrix:
    def __init__(self):
        self.mx_list = []

    def load(self, file_name, separator=' '):
        self.file_to_read = file_name
        self.separator = separator
        if not os.path.exists(self.file_to_read):
            #print('Wrong file name, file doesnt exist')
            return False
        else:
            lines = []
            with open(self.file_to_read, 'r') as file:
                lines = file.readlines()
            for line in lines:
                line = line.replace('\n', '')
                self.mx_list.append(line.split(self.separator))
            for i in range(len(self.mx_list)):
                while('' in self.mx_list[i]):
                    self.mx_list[i].remove('')  
            for i in range(len(self.mx_list)):
                for a in range(len(self.mx_list[i])):
                    if self.mx_list[i][a] == 'None':
                        self.mx_list[i][a] = '*'
            for i in range(len(self.mx_list)-1):
                if len(self.mx_list[i]) != len(self.mx_list[i+1]):
                    return False
                    

            if self.is_digital() == True:
                for i in range(len(self.mx_list)):
                    for a in range(len(self.mx_list[i])):
                        self.mx_list[i][a] = int(self.mx_list[i][a])

            file.close()
            return True

    def size(self):
        try:
            lenght = len(self.mx_list[0])
            height = len(self.mx_list)
            answer = (lenght, height)
        except:
            return False
        return answer

    def is_digital(self):
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
        
        if self.str_t > 0 and self.int_t == 0:
            return False
        elif self.int_t > 0 and self.str_t == 0:
            return True
        else:
            return False

    def save(self, file_name, separator=' '):
        matrix_to_save = self.mx_list
        try:
            with open(file_name, 'w') as file:
                for i in range(len(matrix_to_save)):
                    for a in range(len(matrix_to_save[i])):
                        file.write(str(matrix_to_save[i][a]))
                        file.write(separator)
                    file.write('\n')
            file.close()
            return True
        except:
            return False

    def empty_matrix(self, file_name, x_size=0, y_size=0, separator=' '):
        x = x_size
        y = y_size
        try:
            for i in range(y):
                self.mx_list.append([])
                for a in range(x):
                    self.mx_list[i].append('None')
            self.save(file_name, separator)
            return True
        except:
            return False
    
    def add_value_by_coords(self, x, y, value):
        try:
            self.mx_list[y-1][x-1] = value
            return True
        except:
            return False

    def get_value_by_coords(self, x, y):
        try:
            return self.mx_list[y-1][x-1]
        except:
            return False

    def pretty_print(self):
        line = '                              '
        max_lenght = 0
        try:
            for i in self.mx_list:
                for a in i:
                    if len(str(a)) > max_lenght:
                        max_lenght = len(str(a))

            for i in self.mx_list:
                line = '                              '
                pos = 0
                for a in i:
                    line = line[:pos * (max_lenght+1)] + str(a) + ' ' + line[pos*(max_lenght+1):]
                    pos += 1
                print(line)
                return True
        except:
            return False

    def add_matrixes(self, mx_to_add):
        if self.is_digital() == True and mx_to_add.is_digital() == True:
            if self.size() == mx_to_add.size():
                for i in range(len(self.mx_list)):
                    for a in range(len(self.mx_list[i])):
                                self.mx_list[i][a] = self.mx_list[i][a] + mx_to_add.mx_list[i][a]
                return True
            
        elif self.is_digital() == False and mx_to_add.is_digital() == False:
            if self.size() == mx_to_add.size():
                for i in range(len(self.mx_list)):
                    for a in range(len(self.mx_list[i])):
                                self.mx_list[i][a] = self.mx_list[i][a] + mx_to_add.mx_list[i][a]
                return True
            else:
                return False
        else:
            return False

    def subtrack_matrixes(self, mx_to_subt):
        if self.is_digital() == True and mx_to_subt.is_digital() == True:
            if self.size() == mx_to_subt.size():
                for i in range(len(self.mx_list)):
                    for a in range(len(self.mx_list[i])):
                                self.mx_list[i][a] = self.mx_list[i][a] - mx_to_subt.mx_list[i][a]
                return True

        elif self.is_digital() == False and mx_to_subt.is_digital() == False:
            if self.size() == mx_to_subt.size():
                for i in range(len(self.mx_list)):
                    for a in range(len(self.mx_list[i])):
                        if mx_to_subt.mx_list[i][a] in self.mx_list[i][a]:
                                self.mx_list[i][a] = self.mx_list[i][a].replace(mx_to_subt.mx_list[i][a], '')
                return True
            else:
                return False
        else:
            return False