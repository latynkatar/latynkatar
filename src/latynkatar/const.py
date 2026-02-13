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
in the repo, see <https://github.com/latynkatar/latynkatar/blob/main/LICENSE>.

You should have received a copy of the GNU Lesser General Public License v3
(LGPLv3) along with Łatynkatar. If not, see <https://www.gnu.org/licenses/>.

:copyright: (c) 2025 Łatynkatar group: https://github.com/latynkatar
"""

KIRYLICZNY_ALFABET = [
    "а",
    "б",
    "в",
    "г",
    "ґ",
    "д",
    "е",
    "ё",
    "ж",
    "з",
    "і",
    "й",
    "к",
    "л",
    "м",
    "н",
    "о",
    "п",
    "р",
    "с",
    "т",
    "у",
    "ў",
    "ф",
    "х",
    "ц",
    "ч",
    "ш",
    "ы",
    "ь",
    "э",
    "ю",
    "я",
]
LACINSKI_ALFABET = [
    "a",
    "b",
    "c",
    "ć",
    "č",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "ł",
    "m",
    "n",
    "ń",
    "o",
    "p",
    "r",
    "s",
    "ś",
    "š",
    "t",
    "u",
    "ŭ",
    "v",
    "w",
    "y",
    "z",
    "ź",
    "ž",
    "ż",
]
MOHUC_PAZNACZACCA_JAK_MIAKKIJA = {
    "н": ("n", "ń"),
    "с": ("s", "ś"),
    "ц": ("c", "ć"),
    "з": ("z", "ź"),
    "л": ("ł", "l"),
}
#
# Кірылічныя канстанты
#
HALOSNYJA_CYR = ("а", "е", "ё", "і", "у", "ы", "э", "ю", "я")

PRAVILY_KANVERTACYJ_CYR = {
    "а": "a",
    "э": "e",
    "ы": "y",
    "у": "u",
    "ў": "ŭ",
    "б": "b",
    "в": "v",
    "г": "h",
    "ґ": "g",
    "д": "d",
    "ж": "ž",
    "й": "j",
    "к": "k",
    "м": "m",
    "о": "o",
    "п": "p",
    "р": "r",
    "т": "t",
    "ф": "f",
    "ч": "č",
    "ш": "š",
    "х": "ch",
}
STARYJA_PRAWILY_KANVERTACYJI = dict(PRAVILY_KANVERTACYJ_CYR)
STARYJA_PRAWILY_KANVERTACYJI.update(
    {
        "ч": "cz",
        "ш": "sz",
        "ж": "ż",
        "в": "w",
    }
)
JOTAWANYJA_LITARY = {
    "е": "e",
    "ё": "o",
    "і": "",
    "ю": "u",
    "я": "a",
}
ZYCZNYJA_Z_TRANZITAM = (
    "б",
    "в",
    "д",
    "ж",
    "з",
    "л",
    "м",
    "н",
    "п",
    "р",
    "с",
    "т",
    "ў",
    "ф",
    "ц",
    "ч",
    "ш",
)
ZYCZNYJA_BIEZ_TRANZITU = ("г", "к", "х")


#
# Лацінскія канстанты
#
PRAVILY_KANVERTACYJ_LAT = {
    "y": "ы",
    "ŭ": "ў",
    "b": "б",
    "v": "в",
    "w": "в",
    "g": "ґ",
    "d": "д",
    "ž": "ж",
    "ż": "ж",
    "k": "к",
    "m": "м",
    "p": "п",
    "r": "р",
    "t": "т",
    "f": "ф",
    "č": "ч",
    "š": "ш",
    "ł": "л",
    "h": "г",
    "c": "ц",
    "s": "с",
}

HALOSNYJA_LAT = {
    "e": "э",
    "u": "у",
    "o": "о",
    "a": "а",
}
ZYCZNYJA_DYHRAFY = {
    "ch": "х",
    "sz": "ш",
    "cz": "ч",
}
