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
    HALOSNYJA_CYR,
    JOTAWANYJA_LITARY,
    KIRYLICZNY_ALFABET,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    PRAVILY_KANVERTACYJ_CYR,
    STARYJA_PRAWILY_KANVERTACYJI,
    ZYCZNYJA_Z_TRANZITAM,
)
from .abs_converter import AbstractConverter


class CyrLatConverter(
    AbstractConverter
):  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Класа-канвертар для пераводу кірыліцы ў лацінку.

    :param text: Тэкст які мусіць быць сканвертаваны.
    :type text: str
    """

    def __init__(self, text: str) -> None:
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
        self._old_rules = old_rules
        self._pravily_kanvertacyi = (
            STARYJA_PRAWILY_KANVERTACYJI if self._old_rules else PRAVILY_KANVERTACYJ_CYR
        )
        self._palatalization = palatalization

        return super().convert()

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
                converted_letter = self._kanvertavac_miakkija_zycznyja()
            case letter if letter in ["'", "ь"]:
                pass
            case letter if letter in JOTAWANYJA_LITARY:
                converted_letter = self._kanvertavac_jotavanyja()

        return (
            converted_letter
            if self._symbol.islower()
            else converted_letter.capitalize()
        )

    def _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(self) -> bool:
        """Правярае, ці патрабуе пазіцыя зычнай адлюстравання транзітыўнай мяккасці.

        :return: True, калі патрабуе
        :rtype: bool
        """
        return self._next_symbol.lower() in ZYCZNYJA_Z_TRANZITAM and (
            self._second_next_symbol.lower() in JOTAWANYJA_LITARY
            or self._second_next_symbol.lower() == "ь"
        )

    def _ci_patrabuje_j(self) -> bool:
        """Спраўджае, ці патрэбная пры канвертацыі ётаваных j.

        :return: True, калі патрабуе
        :rtype: bool
        """
        return (
            not self._previos_letters
            or self._previos_letters[-1].lower() in HALOSNYJA_CYR
            or self._previos_letters[-1].lower() in ("'", "ь")
            or self._previos_letters[-1].lower() == "ł"
        )

    def _kanvertavac_jotavanyja(self) -> str:
        """Канвертуе ў лацінку літары з j/i: і, е, ё, ю, я.

        :return: Сканвертаваную да лацінкі літару. Вынікам часам можа быць некалькі літар.
        :rtype: str
        """
        if self._ci_patrabuje_j() and self._symbol.lower() != "і":
            base = "j"
        else:
            base = "i"

        second_letter = JOTAWANYJA_LITARY[self._symbol.lower()]
        if (
            self._symbol.lower() != "і"
            and self._previos_letters
            and self._previos_letters[-1].lower() == "л"
        ):
            base = ""

        converted_letter = base + second_letter

        return converted_letter

    def _kanvertavac_miakkija_zycznyja(self) -> str:
        """Канвертуе да лацінкі зычныя, якія могуць быць мяккімі.

        :return: Вынік канвертацыі
        :rtype: str
        """
        hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[self._symbol.lower()]
        converted_letter = ""
        match True:
            case results if results == (self._next_symbol.lower() == "ь"):
                converted_letter = soft

            case results if results == (
                self._symbol.lower() == "л"
                and self._next_symbol.lower() in JOTAWANYJA_LITARY
            ):
                converted_letter = soft
            case results if results == (
                self._symbol.lower() == self._next_symbol.lower() == "л"
                and (
                    self._second_next_symbol.lower() in JOTAWANYJA_LITARY
                    or self._second_next_symbol.lower() == "ь"
                )
            ):
                converted_letter = soft
            case results if results == (
                self._palatalization
                and self._ci_patrabuje_adlustravannia_tranzityunaj_miakkasci()
                and not (self._symbol == "н" and self._next_symbol == "ц")
            ):
                converted_letter = soft
            case _:
                converted_letter = hard

        return converted_letter

    @property
    def _current_alphabet(self) -> list[str]:
        """Спіс сімвалаў кірылічнага алфавіту.

        :return: Спіс сімвалаў
        :rtype: list[str]
        """
        return KIRYLICZNY_ALFABET
