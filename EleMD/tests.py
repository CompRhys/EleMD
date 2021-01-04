import math
from EleMD import EleMD


def test():
    # values for tests calculated using reference code from https://github.com/lrcfmd/ElMD
    elemd = EleMD("atomic").elemd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), 15.2, abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), 41.2333335, abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), 31.2, abs_tol=1e-5)

    elemd = EleMD("mendeleev").elemd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), 19.6, abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), 25.21666608, abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), 32.6, abs_tol=1e-5)

    elemd = EleMD("pettifor").elemd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), 21.8, abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), 19.50833295, abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), 28.4, abs_tol=1e-5)

    elemd = EleMD("mod_pettifor").elemd
    assert math.isclose(elemd("Zr3AlN", "CaTiO3"), 22.2, abs_tol=1e-5)
    assert math.isclose(elemd("Li7La3Hf2O12", "CsPbI3"), 18.83333291, abs_tol=1e-5)
    assert math.isclose(elemd("Zr3AlN", "CsPbI3"), 31.2, abs_tol=1e-5)

if __name__ == "__main__":
    test()
