import math
from EleMD import EleMD
from ElMD import ElMD


def test_against_reference():
    """
    Test EleMD using POT against reference version.
    """
    elemd = EleMD("atomic").elemd
    elmd = ElMD(metric="atomic").elmd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), elmd("Zr3AlN", "CaTiO3"), abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), elmd("Li7La3Hf2O12", "CsPbI3"), abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), elmd("Zr3AlN", "CsPbI3"), abs_tol=1e-5)

    elemd = EleMD("mendeleev").elemd
    elmd = ElMD(metric="mendeleev").elmd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), elmd("Zr3AlN", "CaTiO3"), abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), elmd("Li7La3Hf2O12", "CsPbI3"), abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), elmd("Zr3AlN", "CsPbI3"), abs_tol=1e-5)

    elemd = EleMD("pettifor").elemd
    elmd = ElMD(metric="petti").elmd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), elmd("Zr3AlN", "CaTiO3"), abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), elmd("Li7La3Hf2O12", "CsPbI3"), abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), elmd("Zr3AlN", "CsPbI3"), abs_tol=1e-5)

    elemd = EleMD("mod_pettifor").elemd
    elmd = ElMD(metric="mod_petti").elmd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), elmd("Zr3AlN", "CaTiO3"), abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), elmd("Li7La3Hf2O12", "CsPbI3"), abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), elmd("Zr3AlN", "CsPbI3"), abs_tol=1e-5)


if __name__ == "__main__":
    test_against_reference()
