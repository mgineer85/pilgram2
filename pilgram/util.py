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

from PIL import Image


def fill(shape, color):
    assert len(shape) == 2
    assert len(color) == 3

    r = Image.new('L', shape, color[0])
    g = Image.new('L', shape, color[1])
    b = Image.new('L', shape, color[2])

    return Image.merge('RGB', (r, g, b))
