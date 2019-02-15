import math

from playLA._global import EPSLION


class Vector:

    # dim表示维度
    @classmethod
    def zero(cls, dim):
        return Vector([0] * dim)

    def __init__(self, lst):
        # list不可更改的类对象
        self._values = list(lst)

    def norm(self):
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        if self.norm() < EPSLION:
            raise ZeroDivisionError
        return Vector(self._values) / self.norm()

    def __repr__(self):
        return "Vector ({})".format(self._values)

    def __str__(self):
        return "({})".format(','.join(str(e) for e in self._values))

    def dot(self, other):
        assert len(other) == len(self), \
            "两个向量不一致"
        return sum(a * b for a, b in zip(self, other))

    def __getitem__(self, item):
        return self._values[item]

    def __len__(self):
        return len(self._values)

    def __iter__(self):
        return self._values.__iter__()

    def __add__(self, other):
        assert len(other) == len(self), \
            "两个向量不一致"

        return Vector((a + b for a, b in zip(self, other)))

    def __sub__(self, other):
        assert len(other) == len(self), \
            "两个向量不一致"

        return Vector((a - b for a, b in zip(self, other)))

    # 乘法要定义正向和反项
    def __mul__(self, other):
        return Vector([other * a for a in self])

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        return (1 / other) * self

    # 向量去正
    def __pos__(self):
        return 1 * self

    # 向量取负
    def __neg__(self):
        return -1 * self
