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

:copyright: (c) 2026 Łatynkatar group: https://github.com/latynkatar
"""

CYRRILIC_ALPHABET = [
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
    "'",
]
LATIN_ALPHABET = [
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
PALATIZEABLE_CONSONANTS = {
    "н": ("n", "ń"),
    "с": ("s", "ś"),
    "ц": ("c", "ć"),
    "з": ("z", "ź"),
    "л": ("ł", "l"),
}
#
# Кірылічныя канстанты
#
CYRRILIC_VOVELS = ("а", "е", "ё", "і", "у", "ы", "э", "ю", "я")

CYR_TO_LAT_CONVERSION = {
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
OLD_CYR_TO_LAT_CONVERSION = dict(CYR_TO_LAT_CONVERSION)
OLD_CYR_TO_LAT_CONVERSION.update(
    {
        "ч": "cz",
        "ш": "sz",
        "ж": "ż",
        "в": "w",
    }
)
IOTATED_VOVELS = {
    "е": "e",
    "ё": "o",
    "і": "",
    "ю": "u",
    "я": "a",
}
CONSONANTS_WITH_PALATALIZATION_TRANSIT = (
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
CONSONANTS_WITHOUT_PALATALIZATION_TRANSIT = ("г", "к", "х")


#
# Лацінскія канстанты
#
LAT_TO_CYR_CONVERSION = {
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

LAT_VOVELS = {
    "e": "э",
    "u": "у",
    "o": "о",
    "a": "а",
}
DIGRAPH_CONSONANTS = {
    "ch": "х",
    "sz": "ш",
    "cz": "ч",
}
