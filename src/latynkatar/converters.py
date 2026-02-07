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

from .const import (
    HALOSNYJA_LAT,
    JOTAWANYJA_LITARY,
    KIRYLICZNY_ALFABET,
    LACINSKI_ALFABET,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    PRAVILY_KANVERTACYJ_CYR,
    PRAVILY_KANVERTACYJ_LAT,
    STARYJA_PRAWILY_KANVERTACYJI,
    ZYCZNYJA_DYHRAFY,
)
from .utils import cyr_to_lat as utils


class CyrLatConverter:  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Класа-канвертар для пераводу кірыліцы ў лацінку.

    :param text: Тэкст які мусіць быць сканвертаваны.
    :type text: str
    """

    def __init__(self, text: str):
        self._text = text
        self._len = len(self._text)
        self._old_rules = False
        self._palatalization = False
        self._in_word_now = False
        self._previos_letters: list[str] = []
        self._pravily_kanvertacyi: dict[str, str]
        self._index: int

    def convert(self, old_rules: bool = False, palatalization: bool = False) -> str:
        """Канвертуе тэкст.

        :param old_rules: Ці трэба ўжываць старыя правілы (з cz, sz і падобнага)
        :type old_rules: bool
        :param palatalization: Ці пазначаць транзіт мяккасці
        :type palatalization: bool
        :return: Сканвертаваны тэкст
        :rtype: str
        """
        converted_text = ""
        self._old_rules = old_rules
        self._pravily_kanvertacyi = (
            STARYJA_PRAWILY_KANVERTACYJI if self._old_rules else PRAVILY_KANVERTACYJ_CYR
        )
        self._palatalization = palatalization

        for self._index in range(  # noqa: B020
            len(self._text)
        ):  # pylint: disable=consider-using-enumerate
            if self._text[self._index].lower() in KIRYLICZNY_ALFABET or (
                self._in_word_now and self._text[self._index] == "'"
            ):
                self._in_word_now = True
                converted_text += self._convert_letter()
                self._previos_letters.append(self._text[self._index])
            else:
                self._in_word_now = False
                converted_text += self._text[self._index]
                self._previos_letters = []
        return converted_text

    def _convert_letter(self) -> str:
        """Канвертаваць адну асобную літару ў адпаведныя сімвалы лацінкі.

        :return: Вынік канвертацыі літары
        :rtype: str
        """
        lowercase_letter = self._symbol.lower()
        converted_letter = ""
        match lowercase_letter:
            case letter if letter in self._pravily_kanvertacyi:
                converted_letter = self._pravily_kanvertacyi[lowercase_letter]
            case letter if letter in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
                converted_letter = utils.kanvertavac_miakkija_zycznyja(
                    simval=self._symbol,
                    nastupny_simval=self._next_symbol,
                    druhi_nastupny=self._second_next_symbol,
                    miakkasc=self._palatalization,
                )
            case letter if letter in ["'", "ь"]:
                pass
            case letter if letter in JOTAWANYJA_LITARY:
                converted_letter = utils.kanvertavac_jotavanyja(
                    self._symbol, self._previos_letters
                )

        return (
            converted_letter
            if self._symbol.islower()
            else converted_letter.capitalize()
        )

    @property
    def _symbol(self) -> str:
        """Бягучы сімвал у часе канвертацыі.

        :return: Бягучы сімвал
        :rtype: str
        """
        return self._text[self._index]

    @property
    def _next_symbol(self) -> str:
        """Наступны симвал.

        :return: Вяртае наступны сімвал, альбо пусты радок, калі наступны сімвал не існуе
        :rtype: str
        """
        return self._text[self._index + 1] if self._index < self._len - 1 else ""

    @property
    def _second_next_symbol(self) -> str:
        """Сімвал праз адзін наперад ад бягучага.

        :return: Вяртае другі наступны сімвал ад бягучага, альбо пусты радок, калі той сімвал не існуе
        :rtype: str
        """
        return self._text[self._index + 2] if self._index < self._len - 2 else ""


class LatCyrConverter:  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Класа-канвертар для пераводу лацінкі ў кірыліцу.

    :param text: Тэкст які мусіць быць сканвертаваны.
    :type text: str
    """

    def __init__(self, text: str):
        self._text = text
        self._len = len(self._text)
        self._in_word_now = False
        self._previos_letters: list[str] = []
        self._pravily_kanvertacyi: dict[str, str]
        self._index: int

    def convert(self) -> str:
        """Канвертуе тэкст.

        :return: Сканвертаваны тэкст
        :rtype: str
        """
        converted_text = ""
        self._pravily_kanvertacyi = PRAVILY_KANVERTACYJ_LAT

        self._index = 0
        while self._index < len(self._text):
            if self._text[self._index].lower() in LACINSKI_ALFABET:
                self._in_word_now = True
                converted_text += self._convert_letter()
                self._previos_letters.append(self._text[self._index])
            else:
                self._in_word_now = False
                converted_text += self._text[self._index]
                self._previos_letters = []
            self._index += 1
        return converted_text

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
                converted_letter = ZYCZNYJA_DYHRAFY[letter + self._next_symbol.lower()]
                skip_one = True
            case letter if letter in self._pravily_kanvertacyi:
                converted_letter = self._pravily_kanvertacyi[lowercase_letter]
            case letter if [
                x for x in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.values() if letter in x
            ]:
                if letter in ("l", "ł"):
                    converted_letter = "л"
                    if (
                        letter == "l"
                        and self._next_symbol not in HALOSNYJA_LAT
                        and self._next_symbol.lower() != ""
                    ):
                        converted_letter += "ь"
                else:
                    letter_variants = [
                        x
                        for x in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.values()
                        if letter in x
                    ][0]
                    converted_letter = [
                        key
                        for key, value in MOHUC_PAZNACZACCA_JAK_MIAKKIJA.items()
                        if value == letter_variants
                    ][0]
                    if letter == letter_variants[-1]:  # калі зычны мяккі
                        converted_letter += "ь"
            case letter if letter in ("i", "j"):
                if self._next_symbol.lower() in HALOSNYJA_LAT:
                    converted_letter = [
                        key
                        for key, value in JOTAWANYJA_LITARY.items()
                        if value == self._next_symbol.lower()
                    ][0]
                    skip_one = True
                elif letter == "j":
                    converted_letter = "й"
                else:
                    converted_letter = "і"
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

    @property
    def _symbol(self) -> str:
        """Бягучы сімвал у часе канвертацыі.

        :return: Бягучы сімвал
        :rtype: str
        """
        return self._text[self._index]

    @property
    def _next_symbol(self) -> str:
        """Наступны симвал.

        :return: Вяртае наступны сімвал, альбо пусты радок, калі наступны сімвал не існуе
        :rtype: str
        """
        return self._text[self._index + 1] if self._index < self._len - 1 else ""

    @property
    def _second_next_symbol(self) -> str:
        """Сімвал праз адзін наперад ад бягучага.

        :return: Вяртае другі наступны сімвал ад бягучага, альбо пусты радок, калі той сімвал не існуе
        :rtype: str
        """
        return self._text[self._index + 2] if self._index < self._len - 2 else ""
