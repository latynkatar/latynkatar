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

from ..const import HALOSNYJA_LAT, JOTAWANYJA_LITARY, MOHUC_PAZNACZACCA_JAK_MIAKKIJA


#
# Канвертацыя літары
#
def convert_miakkija_zycznyja(letter: str, next_symbol) -> str:
    """Канвертуе зычныя, што могуць змякчацца.

    :param letter: літара, што мусіць быць сканвертаваная
    :type letter: str
    :param next_symbol: літараў адразу па ёй у тэксце
    :type next_symbol: _type_
    :return: вынік канвертацыі
    :rtype: str
    """
    converted_letter = ""
    if letter in ("l", "ł"):
        converted_letter = "л"
        if letter == "l" and not (
            next_symbol.lower() in ("i", "j") or next_symbol.lower() in HALOSNYJA_LAT
        ):
            converted_letter += "ь"
    else:
        letter_variants = [
            x for x in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.values() if letter in x
        ][0]
        converted_letter += [
            key
            for key, value in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.items()
            if value == letter_variants
        ][0]
        if letter == letter_variants[-1]:  # калі зычны мяккі
            converted_letter += "ь"

    return converted_letter


def convert_jotavanyja(
    letter: str, previos_letters: list[str], next_symbol: str
) -> tuple[str, bool]:
    """Канвертуе ётаваныя літары да кірыліцы.

    :param letter: літара, што мусіць быць сканвертаваная
    :type letter: str
    :param previos_letters: папярэднія літары слова
    :type previos_letters: list[str]
    :param next_symbol: наступная літара у тэксце па канвертаванай
    :type next_symbol: str
    :return: вынік канвертацыі (літіра  ці некалькі, ці трэба мінаць наступную)
    :rtype: tuple[str, bool]
    """
    converted_letter = ""
    skip_one = False

    if previos_letters and previos_letters[-1].lower() == "ł":
        converted_letter += "'"

    if next_symbol.lower() in HALOSNYJA_LAT:
        if previos_letters and previos_letters[-1].lower() == "l" and letter == "j":
            converted_letter += "ь"

        converted_letter += [
            key
            for key, value in JOTAWANYJA_LITARY.items()
            if value == next_symbol.lower()
        ][0]
        skip_one = True
    elif letter == "j":
        converted_letter += "й"
    else:
        converted_letter += "і"
    return (converted_letter, skip_one)
