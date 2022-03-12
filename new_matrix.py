class New_matrix:
    def __init__(self):
        self.mx = []
        self.line = None
        self.separator = None


    def write_new_mx(self, obj, file, separator):
        self.matrix = obj
        self.filename = file
        if '.' not in self.filename:
            print('Wrong file name')
            return False
        self.separator = separator
        print("Write here your matrix, to end press Enter: ")
        while True:
            self.line = input('>   ')
            if self.line == '\n' or self.line == '':
                break
            else:
                self.line = self.line.split(self.separator)
                while ('' in self.line):
                    self.line.remove('')
                self.mx.append(self.line)
        for i in range(len(self.mx)):
            try:
                if len(self.mx[i]) != len(self.mx[i+1]):
                    print("Your matrix is not correct!")
                    return False
            except IndexError:
                pass
        print(self.mx)
        self.matrix.save(self.matrix, self.filename, self.mx)
        #self.matrix.save(self.matrix, self.filename, self.mx)
        #return self.mx