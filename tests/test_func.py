import pytest
from application.func import berakna_medel, dela

@pytest.mark.parametrize("varde, forvantat", [
    ([1, 2, 3], 2),
    ([10, 20, 30], 20),
    ([5, 15, 25], 15),
    ([0, 0, 0], 0),
    ([-1, -2, -3], -2),
])

def test_berakna_medel(varde, forvantat):
    assert berakna_medel(varde) == forvantat

def test_medel():
    assert berakna_medel([1, 2, 3]) == 2

def test_tom_lista():
    assert berakna_medel([]) == 0

def berakna_medel(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

def test_dela_noll():
    with pytest.raises(ValueError) as e:
        dela(1, 0)
    assert "noll" in str(e.value)
