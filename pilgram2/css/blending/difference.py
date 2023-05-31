# Copyright 2019 Akiomi Kamakura
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PIL import ImageChops

from pilgram2.css.blending.alpha import alpha_blend


def _difference(im1, im2):
    """The difference blend mode.

    Arguments:
        im1: A backdrop image (RGB).
        im2: A source image (RGB).

    Returns:
        The output image.
    """

    return ImageChops.difference(im1, im2)


def difference(im1, im2):
    """Subtracts the darker of the two constituent colors
    from the lighter color.

    The difference formula is defined as:

        B(Cb, Cs) = | Cb - Cs |

    See the W3C document:
    https://www.w3.org/TR/compositing-1/#blendingdifference

    Arguments:
        im1: A backdrop image (RGB or RGBA).
        im2: A source image (RGB or RGBA).

    Returns:
        The output image.
    """

    return alpha_blend(im1, im2, _difference)
