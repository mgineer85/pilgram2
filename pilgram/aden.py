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

from PIL import Image, ImageEnhance, ImageChops

from pilgram.hue_rotate import hue_rotate
from pilgram import util


def aden(im):
    cb = im.convert('RGB')

    cs = util.fill(cb.size, [66, 10, 14])
    cs = ImageChops.darker(cb, cs)

    alpha_mask = util.linear_gradient_mask(cb.size, start=.8, end=1)
    cr = Image.composite(cb, cs, alpha_mask)

    cr = hue_rotate(cr, -20)
    cr = ImageEnhance.Contrast(cr).enhance(.9)
    cr = ImageEnhance.Color(cr).enhance(.85)
    cr = ImageEnhance.Brightness(cr).enhance(1.2)

    return cr.convert(im.mode)