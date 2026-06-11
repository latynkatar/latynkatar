"""
Гэты модуль змяшчае ўсе даступныя канвертары.

У гэты момант даступныя:
- LatCyrConverter для канвертацыі з лацінкі ў кірыліцу.
- CyrLatConverter для канвертацыі з кірыліцы ў лацінку.


This file is part of Łatynkatar.

Latynkatar is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Łatynkatar is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/latynkatar/latynkatar/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) 2025 Łatynkatar group: https://github.com/latynkatar
"""

from .cyr_lat import CyrLatConverter
from .lat_cyr import LatCyrConverter

__all__ = ["CyrLatConverter", "LatCyrConverter"]
