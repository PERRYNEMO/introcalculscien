from tp_warmup.produit import *

def test_produit():
    assert produit([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert produit([3.4, 0], [2.34]) == [(3.4, 2.34), (0, 2.34)]
    assert produit([1, 2], []) == []
    assert produit([], []) == []

def test_power_set():
    assert power_set([1]) == [[], [1]]
    assert power_set([1, 2]) == [[], [2], [1], [1, 2]]
    assert power_set([]) == [[]]