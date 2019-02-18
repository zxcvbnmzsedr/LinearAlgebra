from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print('matrix.shape = {}'.format(matrix.shape()))
    print('matrix.size = {}'.format(matrix.size()))
    print('len(matrix) = {}'.format(len(matrix)))
    print('matrix[0][0] = {}'.format(matrix[0, 0]))

    matrix2 = Matrix([[5, 6], [7, 8]])

    print(matrix + matrix2)
    print(matrix - matrix2)

    print(5 * matrix)

    print(matrix / 2)

    print(Matrix.zero(2, 3))
