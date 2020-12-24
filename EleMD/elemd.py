import numpy as np

from ot import emd2
from pymatgen import Composition

from ElMD.scales import (
    pymatgen_els,
    atomic,
    mendeleev,
    petti,
    mod_petti,
)


class EleMD:
    # TODO allow for custom scale_dicts
    def __init__(self, scale: str = "mod_pettifor"):
        """[summary]

        Args:
            scale (str, optional): Name of chemical scale to
            use to calculate cost Matrix. Defaults to "mod_pettifor".
            ["atomic", "mendeleev", "pettifor", "mod_pettifor"] are allowed.
        """
        self.scale = scale
        self.M = _get_cost_matrix(scale)

    def elemd(self, comp1: str, comp2: str):
        """returns the EleMD between two compositions
        """
        x1 = _get_frac_vector(comp1)
        x2 = _get_frac_vector(comp2)

        return emd2(x1, x2, self.M)


def _get_frac_vector(comp: str):
    py_comp = Composition(comp)

    vector = np.zeros(103)
    for el in py_comp.element_composition.fractional_composition.items():
        vector[el[0].number - 1] = el[1]

    return vector


def _get_cost_matrix(scale: str):
    scale = scale.lower()

    if scale == "atomic":
        v_scale = [atomic[el] for el in pymatgen_els]
    elif scale == "mendeleev":
        v_scale = [mendeleev[el] for el in pymatgen_els]
    elif scale == "pettifor":
        v_scale = [petti[el] for el in pymatgen_els]
    elif scale == "mod_pettifor":
        v_scale = [mod_petti[el] for el in pymatgen_els]
    else:
        raise ValueError

    v_scale = np.atleast_2d(v_scale)
    ones = np.ones_like(v_scale)
    return np.abs(np.matmul(v_scale.T, ones) - np.matmul(ones.T, v_scale))
