class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        matrix = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(matrix)

    def __str__(self):
        s = ""
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(matrix_1 + matrix_2)