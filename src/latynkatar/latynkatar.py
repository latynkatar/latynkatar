"""
This file is part of Łatynkatar.

Łatynkatar is free software: you can redistribute it and/or modify it under the
terms of the GNU Lesser General Public License v3 (LGPLv3) as published by the
Free Software Foundation, either version 3 of the License, or (at your option)
any later version.

Łatynkatar is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License v3 (LGPLv3) for
more details. In file LICENSE which should came with a package, or look at it
in the repo, see <https://github.com/measles/latynkatar/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) (c) 2025 Łatynkatar group: https://github.com/latynkatar
"""

from .converters import CyrLatConverter


def convert(text: str, miakkasc: bool = True) -> str:
    """Канвертуе з кірыліцы да сучаснай ("чэшскай") лацінкі. Усе літары і знакі, які не могуць
        лічыцца беларускай кірыліцай захоўваюцца без зменаў.


    Args:
        text (str): Тэкст які мусіць быць сканвертаваны
        miakkasc (bool, optional): Ці пазначаць транзітыўную мяккасць.
            Па змоўчванню True.

    Returns:
        str: Вынік канвертацыі
    """
    return CyrLatConverter(text=text).convert(old_rules=False, palatalization=miakkasc)


def convert_old(text: str, miakkasc: bool = True) -> str:
    """Канвертуе з кірыліцы да старой ("польскай") лацінкі. Усе літары і знакі, які не могуць
        лічыцца беларускай кірыліцай захоўваюцца без зменаў.


    Args:
        text (str): Тэкст, які мусіць быць сканвертаваны.
        miakkasc (bool, optional): Ці пазначаць транзітыўную мяккасць.
            Па змоўчваннб True.

    Returns:
        str: Вынік канвертацыі
    """
    return CyrLatConverter(text=text).convert(old_rules=True, palatalization=miakkasc)
