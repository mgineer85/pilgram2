# pilgram2

[![PyPI](https://img.shields.io/pypi/v/pilgram2.svg)](https://python.org/pypi/pilgram2)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pilgram2.svg)](https://python.org/pypi/pilgram2)
[![Python CI](https://github.com/mgineer85/pilgram2/actions/workflows/ci.yml/badge.svg)](https://github.com/mgineer85/pilgram2/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mgineer85/pilgram2/branch/main/graph/badge.svg)](https://codecov.io/gh/mgineer85/pilgram2)

A python library for instagram filters.

![screenshot](https://raw.githubusercontent.com/mgineer85/pilgram2/main/screenshots/screenshot.png)

The filter implementations are inspired by [CSSgram](https://una.im/CSSgram/).
Pilgram2 was forked from [pilgram](https://github.com/akiomik/pilgram).
Pilgram2 features more filter and supports non-quadratic images.

## Requirements

- Python >= 3.9
- [Pillow](https://pillow.readthedocs.io/en/stable/) or [pillow-simd](https://github.com/uploadcare/pillow-simd)
- [NumPy](https://numpy.org)

## Install

```sh
pip install pillow # or pip install pillow-simd
pip install numpy
pip install pilgram2
```

## Usage

39 available instagram filters on `pilgram2`, 14 filters new to pilgram2 compared to pilgram:

- `_1977`
- `aden`
- `ashby` (new in pilgram2)
- `amaro` (new in pilgram2)
- `brannan`
- `brooklyn`
- `charmes` (new in pilgram2)
- `clarendon`
- `crema` (new in pilgram2)
- `dogpatch` (new in pilgram2)
- `earlybird`
- `gingham`
- `ginza` (new in pilgram2)
- `hefe` (new in pilgram2)
- `helena` (new in pilgram2)
- `hudson`
- `inkwell`
- `juno` (new in pilgram2)
- `kelvin`
- `lark`
- `lofi`
- `ludwig` (new in pilgram2)
- `maven`
- `mayfair`
- `moon`
- `nashville`
- `perpetua`
- `poprocket` (new in pilgram2)
- `reyes`
- `rise`
- `sierra` (new in pilgram2)
- `skyline` (new in pilgram2)
- `slumber`
- `stinson`
- `sutro` (new in pilgram2)
- `toaster`
- `valencia`
- `walden`
- `willow`
- `xpro2`

```python
from PIL import Image
import pilgram2

im = Image.open('sample.jpg')
pilgram2.aden(im).save('sample-aden.jpg')
```

Similarly, pilgram2 provides css filters and blend modes as a by-product.

Available css filters on `pilgram2.css`:

- `contrast`
- `grayscale`
- `hue_rotate`
- `saturate`
- `sepia`

```python
from PIL import Image
import pilgram2.css

im = Image.open('sample.jpg')
pilgram2.css.sepia(im).save('sample-sepia.jpg')
```

Available blend modes on `pilgram2.css.blending`:

- `color`
- `color_burn`
- `color_dodge`
- `darken`
- `difference`
- `exclusion`
- `hard_light`
- `hue`
- `lighten`
- `multiply`
- `normal`
- `overlay`
- `screen`
- `soft_light`

```python
from PIL import Image
import pilgram2.css.blending

backdrop = Image.open('backdrop.jpg')
source = Image.open('source.jpg')
pilgram2.css.blending.color(backdrop, source).save('blending.jpg')
```

## Test

```sh
pipenv install --dev
make test     # pytest
```
