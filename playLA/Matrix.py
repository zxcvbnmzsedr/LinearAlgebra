from playLA.Vector import Vector


class Matrix:

    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    def __repr__(self):
        return 'Matrix ({})'.format(self._values)

    __str__ = __repr__

    def shape(self):
        return len(self._values), len(self._values[0])

    def size(self):
        r, s = self.shape()
        return r * s

    def __getitem__(self, pos):
        r, s = pos
        return self._values[r][s]

    def row_num(self):
        return self.shape()[0]

    __len__ = row_num

    def cell_num(self):
        return self.shape()[1]

    def row_vector(self, index):
        return Vector(self._values[index])

    def cell_vector(self, index):
        return Vector(row[index] for row in self._values)

    def __add__(self, other):
        assert self.shape() == other.shape(), \
            "ERROR ADD ,Shape Of matrix must be same"
        return Matrix([a + b for a, b in zip(self.row_vector(i),
                                             other.row_vector(i))]
                      for i in range(self.row_num()))

    def __sub__(self, other):
        assert self.shape() == other.shape(), \
            "ERROR SUB ,Shape Of matrix must be same"
        return Matrix([a - b for a, b in zip(self.row_vector(i),
                                             other.row_vector(i))]
                      for i in range(self.row_num()))

    def __mul__(self, k):
        return Matrix([[k * b for b in self.row_vector(i)]
                       for i in range(self.row_num())])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return (1 / other) * self

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    @classmethod
    def zero(cls, r, c):
        """r行c列的0矩阵"""

        return cls([[0] * c for _ in range(r)])
