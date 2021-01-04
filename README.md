# EleMD

![Tests](https://github.com/CompRhys/EleMD/workflows/Tests/badge.svg)

A minimal implementation of the Element-Movers-Distance using standard libraries.

This repository provides an implementations of the Element-Movers-Distance as described in the paper "[The Earth Movers Distance as a metric for the space of inorganic compositions](https://chemrxiv.org/articles/preprint/The_Earth_Mover_s_Distance_as_a_Metric_for_the_Space_of_Inorganic_Compositions/12777566)".

## Installation

To install:

```bash
git clone https://github.com/CompRhys/EleMD
cd EleMD
python setup.py sdist
pip install -e .
```

## Usage
For simple usage initiate an object with a chemical scale

```python
from EleMD import EleMD
mod_petti = EleMD(scale="mod_pettifor")
```

Calculate the distance to a second object with the `elemd` method.

```python
print(mod_petti.elemd("SrTiO3", "CaTiO3"))
```

Alternate chemical scales may be accessed via the "scale" argument, e.g.

```python
atomic = EleMD(scale="atomic")
```

## Disclaimer

This code is designed to mimic the functionality of this reference implementation https://github.com/lrcfmd/ElMD. We do not have any involvement in the development of that code nor any claim to the idea of the element-movers-distance.

This is research code shared without support or any guarantee on its quality. However, please do raise an issue or submit a pull request if you spot something wrong or that could be improved.
