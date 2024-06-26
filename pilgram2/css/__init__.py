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

from pilgram2.css import blending  # noqa
from pilgram2.css.brightness import brightness
from pilgram2.css.contrast import contrast
from pilgram2.css.grayscale import grayscale
from pilgram2.css.hue_rotate import hue_rotate
from pilgram2.css.saturate import saturate
from pilgram2.css.sepia import sepia

__all__ = ["brightness", "contrast", "grayscale", "hue_rotate", "saturate", "sepia"]
