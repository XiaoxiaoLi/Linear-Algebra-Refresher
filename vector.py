class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        try:
            if self.dimension != v.dimension:
                raise ValueError
            return Vector(sum(x) for x in zip(self.coordinates, v.coordinates))

        except ValueError:
            raise ValueError('The vector dimensions must be the same: dimension: '+ str(self.dimension)+" given vector dimension: "+str(v.dimension))

