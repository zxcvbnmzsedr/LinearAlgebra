from playLA.Matrix import Matrix
from playLA.Vector import Vector

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

    print(matrix.dot(matrix2))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print(T.dot(p))
    p = Matrix([[0, 4, 5], [0, 0, 3]])
    print(T.dot(p))

