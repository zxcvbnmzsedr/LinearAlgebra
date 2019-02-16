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
