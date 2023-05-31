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

from pilgram2 import util


def test_add():
    im1 = util.fill((2, 2), [0, 127, 255])
    im2 = util.fill((2, 2), [0, 127, 255])

    actual = util.add(im1, im2)
    expected = util.fill((2, 2), [0, 254, 255])
    assert actual == expected


def test_add2():
    im1 = util.fill((2, 2), [0, 127, 255])
    im2 = util.fill((2, 2), [0, 127, 255])

    actual = util.add(im1, im2)
    expected = ImageChops.add(im1, im2)
    assert actual == expected
