""" """


def produit[X, Y](x: list[X], y:list[Y] ) -> list[tuple[X, Y]]:
    """
    Cartesian product of two sets
    :param x: set X
    :param y: set Y
    :return: cartesian product of X and Y
    """
    return [(i,j) for i in x for j in y]

def power_set[X](x: list[X]) -> list[list[X]]:
    """
    The power set of the set X
    :param x: set X
    :return: power set of X
    """
    if len(x) == 0:
        return [[]]
    p = power_set(x[1:])
    return p + [[x[0]]+y for y in p]