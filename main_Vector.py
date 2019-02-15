from playLA.Vector import Vector

if __name__ == '__main__':
    vector = Vector([4, 3])

    vector2 = Vector([3, 4])

    print("{} + {} = {}".format(vector, vector2, vector + vector2))

    print("{} - {} = {}".format(vector, vector2, vector - vector2))

    print("{} * {} = {}".format(vector, 5, vector * 5))

    print("{} * {} = {}".format(5, vector, 5 * vector))

    zero2 = Vector.zero(5)

    print(zero2)

    print(vector.norm())
    print(zero2.normalize().norm())
