# pilgram2

[![PyPI](https://img.shields.io/pypi/v/pilgram2.svg)](https://python.org/pypi/pilgram2)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pilgram2.svg)](https://python.org/pypi/pilgram2)
[![Python CI](https://github.com/mgineer85/pilgram2/actions/workflows/ci.yml/badge.svg)](https://github.com/mgineer85/pilgram2/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/mgineer85/pilgram2/branch/main/graph/badge.svg)](https://codecov.io/gh/mgineer85/pilgram2)

A python library for instagram-like filters.

![screenshot](https://raw.githubusercontent.com/mgineer85/pilgram2/main/screenshots/screenshot.png)

The filter implementations are inspired by [CSSgram](https://una.im/CSSgram/).
Pilgram2 was forked from [pilgram](https://github.com/akiomik/pilgram).
Pilgram2 features more filter and supports non-quadratic images.

## Requirements

- Python >= 3.10
- [Pillow](https://pillow.readthedocs.io/en/stable/) or [pillow-simd](https://github.com/uploadcare/pillow-simd)
- [NumPy](https://numpy.org)

## Install

```sh
pip install pilgram2
```

Numpy2 and Pillow are installed automatically as dependency.

## Usage

40 available instagram-like filters on `pilgram2`, 14 filters new to pilgram2 compared to pilgram:

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

## Performance

For the benchmark a jpg with 1MP resolution is used.

```text
---------------------------------------------------------------------------------------------- benchmark: 40 tests ----------------------------------------------------------------------------------------------
Name (time in ms)     Min                 Max                Mean             StdDev              Median                IQR            Outliers      OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[inkwell]        14.7927 (1.0)       16.6190 (1.0)       15.6007 (1.0)       0.3851 (1.0)       15.6317 (1.0)       0.4684 (1.0)          13;1  64.0999 (1.0)          48           1
[dogpatch]       14.9385 (1.01)      27.9690 (1.68)      21.4696 (1.38)      3.7996 (9.87)      21.2801 (1.36)      6.2587 (13.36)        13;0  46.5776 (0.73)         34           1
[skyline]        16.3814 (1.11)      17.7252 (1.07)      17.0030 (1.09)      0.4540 (1.18)      16.9221 (1.08)      0.8369 (1.79)         21;0  58.8132 (0.92)         45           1
[aden]           22.8311 (1.54)      26.1220 (1.57)      24.4786 (1.57)      0.8899 (2.31)      24.5015 (1.57)      1.4040 (3.00)         12;0  40.8520 (0.64)         33           1
[valencia]       32.2682 (2.18)      43.2957 (2.61)      35.3279 (2.26)      3.2645 (8.48)      34.0272 (2.18)      2.6154 (5.58)          4;4  28.3062 (0.44)         27           1
[toaster]        32.3596 (2.19)      51.7326 (3.11)      36.0827 (2.31)      5.1677 (13.42)     33.7007 (2.16)      3.2853 (7.01)          4;4  27.7141 (0.43)         26           1
[walden]         32.9225 (2.23)      35.5271 (2.14)      33.9094 (2.17)      0.5789 (1.50)      33.9418 (2.17)      0.9279 (1.98)          6;0  29.4903 (0.46)         26           1
[lofi]           33.7358 (2.28)      45.3981 (2.73)      39.7595 (2.55)      4.3715 (11.35)     39.8462 (2.55)      8.1678 (17.44)        10;0  25.1512 (0.39)         21           1
[hudson]         41.5267 (2.81)      65.5077 (3.94)      52.2767 (3.35)      6.0362 (15.67)     51.8195 (3.32)      5.3300 (11.38)         8;2  19.1290 (0.30)         22           1
[brannan]        41.7347 (2.82)      67.3481 (4.05)      51.5823 (3.31)      8.6528 (22.47)     50.6219 (3.24)     15.7990 (33.73)         7;0  19.3865 (0.30)         18           1
[_1977]          46.3952 (3.14)      50.3905 (3.03)      47.5096 (3.05)      1.0633 (2.76)      47.2432 (3.02)      1.4271 (3.05)          5;1  21.0484 (0.33)         17           1
[amaro]          49.2423 (3.33)      71.3877 (4.30)      55.6583 (3.57)      6.3662 (16.53)     53.8839 (3.45)      9.9413 (21.22)         5;0  17.9668 (0.28)         19           1
[ashby]          49.4625 (3.34)      85.7994 (5.16)      64.9605 (4.16)     12.1187 (31.47)     60.5546 (3.87)     20.2487 (43.22)         5;0  15.3940 (0.24)         16           1
[charmes]        60.0321 (4.06)     101.8152 (6.13)      83.7023 (5.37)     11.5269 (29.93)     85.8406 (5.49)     13.6261 (29.09)         4;0  11.9471 (0.19)         12           1
[ginza]          63.5919 (4.30)      75.3636 (4.53)      69.4724 (4.45)      3.5722 (9.28)      70.7299 (4.52)      5.0449 (10.77)         4;0  14.3942 (0.22)         14           1
[perpetua]       63.6445 (4.30)     127.1038 (7.65)      86.4235 (5.54)     23.4845 (60.98)     81.3043 (5.20)     45.7517 (97.67)         2;0  11.5709 (0.18)         10           1
[ludwig]         64.4726 (4.36)      75.3857 (4.54)      67.2462 (4.31)      3.1901 (8.28)      66.0117 (4.22)      1.3184 (2.81)          2;2  14.8707 (0.23)         14           1
[helena]         69.0363 (4.67)      74.9969 (4.51)      71.1920 (4.56)      1.8539 (4.81)      70.6489 (4.52)      1.9596 (4.18)          4;2  14.0465 (0.22)         14           1
[reyes]          69.1557 (4.67)     139.6323 (8.40)      82.6743 (5.30)     18.6275 (48.37)     78.3593 (5.01)      8.5253 (18.20)         1;1  12.0957 (0.19)         12           1
[sierra]         69.4793 (4.70)      79.2627 (4.77)      72.5720 (4.65)      2.7665 (7.18)      71.9568 (4.60)      3.4747 (7.42)          3;1  13.7794 (0.21)         13           1
[moon]           73.1526 (4.95)      89.4248 (5.38)      79.3208 (5.08)      5.3625 (13.92)     78.0548 (4.99)      2.7963 (5.97)          4;2  12.6070 (0.20)         11           1
[sutro]          74.9125 (5.06)      81.8404 (4.92)      78.7309 (5.05)      2.2877 (5.94)      78.6869 (5.03)      3.6564 (7.81)          4;0  12.7015 (0.20)         13           1
[poprocket]      75.8234 (5.13)      93.3793 (5.62)      81.3538 (5.21)      5.3575 (13.91)     80.3932 (5.14)      5.1918 (11.08)         3;1  12.2920 (0.19)         10           1
[gingham]        76.5663 (5.18)     112.4626 (6.77)      96.1028 (6.16)     11.3066 (29.36)     96.7066 (6.19)     14.5940 (31.15)         4;0  10.4055 (0.16)         11           1
[clarendon]      78.6327 (5.32)     105.2616 (6.33)      90.5513 (5.80)      8.8493 (22.98)     91.5524 (5.86)     14.9693 (31.95)         5;0  11.0435 (0.17)         12           1
[juno]           79.5454 (5.38)      86.3897 (5.20)      82.7420 (5.30)      1.8151 (4.71)      82.6390 (5.29)      1.6914 (3.61)          4;1  12.0858 (0.19)         12           1
[hefe]           80.7009 (5.46)     108.9027 (6.55)      97.7954 (6.27)      7.8742 (20.45)    100.0063 (6.40)      8.0825 (17.25)         2;1  10.2254 (0.16)         10           1
[crema]          83.6725 (5.66)     128.3671 (7.72)     107.8763 (6.91)     17.2011 (44.66)    108.5212 (6.94)     31.9837 (68.28)         5;0   9.2699 (0.14)         11           1
[earlybird]      88.0627 (5.95)     125.7052 (7.56)      99.1542 (6.36)     10.7730 (27.97)     97.7716 (6.25)      8.1004 (17.29)         3;1  10.0853 (0.16)         10           1
[stinson]        88.1440 (5.96)      92.5163 (5.57)      90.3443 (5.79)      1.2374 (3.21)      90.2882 (5.78)      1.7461 (3.73)          2;0  11.0688 (0.17)         11           1
[nashville]      92.2324 (6.23)     107.8121 (6.49)      97.5752 (6.25)      4.3606 (11.32)     96.3156 (6.16)      2.9587 (6.32)          2;1  10.2485 (0.16)         10           1
[lark]          115.7711 (7.83)     130.7196 (7.87)     122.7348 (7.87)      5.8105 (15.09)    123.5049 (7.90)     10.4515 (22.31)         4;0   8.1476 (0.13)          7           1
[slumber]       118.1546 (7.99)     127.5657 (7.68)     120.9845 (7.76)      3.0562 (7.94)     120.3488 (7.70)      3.1461 (6.72)          1;1   8.2655 (0.13)          8           1
[kelvin]        121.3913 (8.21)     166.8817 (10.04)    145.5299 (9.33)     17.3556 (45.06)    151.9569 (9.72)     28.6256 (61.11)         4;0   6.8714 (0.11)          9           1
[xpro2]         132.8882 (8.98)     146.0725 (8.79)     137.4924 (8.81)      4.0534 (10.52)    137.2480 (8.78)      3.8250 (8.17)          2;1   7.2731 (0.11)          8           1
[brooklyn]      143.4111 (9.69)     193.0370 (11.62)    167.2185 (10.72)    19.9176 (51.72)    162.1767 (10.37)    36.4878 (77.89)         3;0   5.9802 (0.09)          6           1
[rise]          177.4342 (11.99)    195.9506 (11.79)    187.4728 (12.02)     7.7946 (20.24)    190.5401 (12.19)    12.8336 (27.40)         2;0   5.3341 (0.08)          5           1
[mayfair]       182.9677 (12.37)    198.1317 (11.92)    189.4664 (12.14)     6.7786 (17.60)    186.4418 (11.93)    11.7959 (25.18)         1;0   5.2780 (0.08)          5           1
[willow]        185.9956 (12.57)    206.6348 (12.43)    193.8252 (12.42)     7.0351 (18.27)    192.6173 (12.32)     4.8559 (10.37)         2;1   5.1593 (0.08)          6           1
[maven]         302.5935 (20.46)    343.4470 (20.67)    328.5673 (21.06)    18.5146 (48.07)    338.5386 (21.66)    30.7547 (65.65)         1;0   3.0435 (0.05)          5           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

## Test

```sh
pipenv install --dev
make test     # pytest
```
