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

from ..const import (
    HALOSNYJA_LAT,
    JOTAWANYJA_LITARY,
    LACINSKI_ALFABET,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    PRAVILY_KANVERTACYJ_LAT,
    ZYCZNYJA_DYHRAFY,
)
from .abs_converter import AbstractConverter


class LatCyrConverter(
    AbstractConverter
):  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Класа-канвертар для пераводу лацінкі ў кірыліцу.

    :param text: Тэкст які мусіць быць сканвертаваны.
    :type text: str
    """

    def __init__(self, text: str):
        self._text = text
        self._len = len(self._text)
        self._in_word_now = False
        self._previos_letters: list[str] = []
        self._pravily_kanvertacyi: dict[str, str] = PRAVILY_KANVERTACYJ_LAT
        self._index: int

    def _convert_letter(self) -> str:  # pylint: disable=too-many-branches
        """Канвертаваць адну асобную літару ў адпаведныя сімвалы кірыліцы.

        :return: Вынік канвертацыі літары
        :rtype: str
        """
        lowercase_letter = self._symbol.lower()
        converted_letter = ""
        skip_one = False
        match lowercase_letter:
            case letter if letter + self._next_symbol.lower() in ZYCZNYJA_DYHRAFY:
                if (
                    self._previos_letters
                    and self._previos_letters[-1].lower() == "l"
                    and letter == "j"
                ):
                    converted_letter += "ь"
                converted_letter += ZYCZNYJA_DYHRAFY[letter + self._next_symbol.lower()]
                skip_one = True
            case letter if letter in self._pravily_kanvertacyi:
                converted_letter = self._pravily_kanvertacyi[lowercase_letter]
            case letter if [
                x for x in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.values() if letter in x
            ]:
                converted_letter = self._convert_miakkija_zycznyja()
            case letter if letter in ("i", "j"):
                converted_letter, skip_one = self._convert_jotavanyja()
            case letter if letter in HALOSNYJA_LAT:
                if self._previos_letters and self._previos_letters[-1].lower() == "l":
                    converted_letter = [
                        key
                        for key, value in JOTAWANYJA_LITARY.items()
                        if letter == value
                    ][0]
                else:
                    converted_letter = HALOSNYJA_LAT[letter]

        converted_results = (
            converted_letter
            if self._symbol.islower()
            else converted_letter.capitalize()
        )

        if skip_one:
            self._index += 1

        return converted_results

    def _convert_miakkija_zycznyja(self) -> str:
        """Канвертуе зычныя, што могуць змякчацца.

        :return: вынік канвертацыі
        :rtype: str
        """
        converted_letter = ""
        if self._symbol.lower() in ("l", "ł"):
            converted_letter = "л"
            if self._symbol.lower() == "l" and not (
                self._next_symbol.lower() in ("i", "j")
                or self._next_symbol.lower() in HALOSNYJA_LAT
            ):
                converted_letter += "ь"
        else:
            key, values = [
                (index, value)
                for index, value in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.items()
                if self._symbol.lower() in value
            ][0]
            converted_letter += key
            _, miakki = values
            if self._symbol.lower() == miakki:
                converted_letter += "ь"

        return converted_letter

    def _convert_jotavanyja(self) -> tuple[str, bool]:
        """Канвертуе ётаваныя літары да кірыліцы.

        :return: вынік канвертацыі (літара  ці некалькі, ці трэба мінаць наступную)
        :rtype: tuple[str, bool]
        """
        converted_letter = ""
        skip_one = False

        if self._previos_letters and self._previos_letters[-1].lower() == "ł":
            converted_letter += "'"

        if self._next_symbol.lower() in HALOSNYJA_LAT:
            if (
                self._previos_letters
                and self._previos_letters[-1].lower() == "l"
                and self._symbol == "j"
            ):
                converted_letter += "ь"

            converted_letter += [
                key
                for key, value in JOTAWANYJA_LITARY.items()
                if value == self._next_symbol.lower()
            ][0]
            skip_one = True
        elif self._symbol.lower() == "j":
            converted_letter += "й"
        else:
            converted_letter += "і"
        return (converted_letter, skip_one)

    @property
    def _current_alphabet(self) -> list[str]:
        """Спіс сімвалаў лацінкі.

        :return: Спіс сімвалаў
        :rtype: list[str]
        """
        return LACINSKI_ALFABET
