class Matrix:
    def __init__(self, matrix_string):
        self.rows = [[int(x) for x in i.split()] for i in matrix_string.split('\n')] 
        self.columns = [list(l) for l in zip(*self.rows)]
    
    def row(self, row):
        return self.rows[row-1]

    def column(self, column):
        return self.columns[column-1]
