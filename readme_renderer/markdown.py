# Copyright 2014 Donald Stufft
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, division, print_function

import cmarkgfm

from .clean import clean


variants = {
    "GFM": cmarkgfm.github_flavored_markdown_to_html,
    "CommonMark": cmarkgfm.markdown_to_html,
}


def render(raw, variant="GFM", **kwargs):
    renderer = variants.get(variant)

    if renderer:
        rendered = renderer(raw)

        if rendered:
            return clean(rendered)

    return None
