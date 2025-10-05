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

from .const import (
    HALOSNYJA,
    JOTAWANYJA_LITARY,
    KIRYLICZNY_ALFABET,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    PRAVILY_KANVERTACYJ,
    STARYJA_PRAWILY_KANVERTACYJI,
    ZYCZNYJA_Z_TRANZITAM,
)


class CyrLatConverter:  # pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Kłasa kab kanvertavać kiryličny tekst da łacinki."""

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
        """Biezpasredna vykonvaje kanvertacyju tekstu.

        :param old_rules: Ci treba užyvać staryja praviły (z cz, sz i da t.p.)
        :type old_rules: bool
        :param palatalization: Ci paznaczać tranzityŭnuju miakkaść
        :type palatalization: bool
        """
        converted_text = ""
        self._old_rules = old_rules
        self._pravily_kanvertacyi = (
            STARYJA_PRAWILY_KANVERTACYJI if self._old_rules else PRAVILY_KANVERTACYJ
        )
        self._palatalization = palatalization

        for index in range(len(self._text)):  # pylint: disable=consider-using-enumerate
            self._index = index
            if self._text[index].lower() in KIRYLICZNY_ALFABET or (
                self._in_word_now and self._text[index] == "'"
            ):
                self._in_word_now = True
            else:
                self._in_word_now = False

            if self._in_word_now:
                converted_text += self._convert_letter()
                self._previos_letters.append(self._text[index])
            else:
                converted_text += self._text[index]
                self._previos_letters = []

        return converted_text

    def _convert_letter(self) -> str:
        """Kanviertuje adzin simvał u adpavednyja simvały łacinki."""
        lowercase_letter = self._text[self._index].lower()
        converted_letter = ""
        match lowercase_letter:
            case letter if letter in self._pravily_kanvertacyi:
                converted_letter = self._pravily_kanvertacyi[lowercase_letter]
            case letter if letter in MOHUC_PAZNACZACCA_JAK_MIAKKIJA:
                converted_letter = self._miakkuja_zycznyja()
            case letter if letter in ["'", "ь"]:
                pass
            case letter if letter in JOTAWANYJA_LITARY:
                converted_letter = self._kanvertavac_z_j()

        return (
            converted_letter
            if self._text[self._index].islower()
            else converted_letter.capitalize()
        )

    def _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(self) -> bool:
        """Правярае, ці патрабуе пазіцыя зычнай адлюстравання транзітыўнай мяккасці.
        Returns:
            bool: True, калі патрабуе
        """
        return self._text[self._index + 1].lower() in ZYCZNYJA_Z_TRANZITAM and (
            self._text[self._index + 2].lower() in JOTAWANYJA_LITARY
            or self._text[self._index + 2].lower() == "ь"
        )

    def _ci_patrabuje_j(self) -> bool:
        """Спраўджае, ці патрэбная пры канвертацыі ётаваных j.
        Returns:
            bool: True, калі патрабуе
        """
        return (
            not self._text[self._index - 1]
            or self._text[self._index - 1].lower() in HALOSNYJA
            or not self._text[self._index - 1].isalpha()
            or self._text[self._index - 1] == "'"
            or self._text[self._index - 1] == "ь"
        )

    def _kanvertavac_z_j(self) -> str:
        """Канвертуе ў лацінку літары з j/i: і, е, ё, ю, я.
        Returns:
            str: Сканвертаваную да лацінкі літару. Вынікам часцяком можа быць
                некалькі літар.
        """
        if self._ci_patrabuje_j() and self._text[self._index].lower() != "і":
            base = "j"
        else:
            base = "i"

        second_letter = JOTAWANYJA_LITARY[self._text[self._index].lower()]
        if (
            self._text[self._index].lower() != "і"
            and self._index > 1
            and self._text[self._index - 1].lower() == "л"
        ):
            base = ""

        converted_letter = base + second_letter

        return converted_letter

    def _miakkuja_zycznyja(self) -> str:
        """Канвертуе да лацінкі зычныя, якія могуць быць мяккімі.

        Returns:
            str: вынік канвертацыі
        """
        hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[self._text[self._index].lower()]
        converted_letter = ""
        if self._index < self._len - 1 and self._text[self._index + 1].lower() == "ь":
            converted_letter = soft
        elif (
            self._index < self._len - 1
            and self._text[self._index].lower() == "л"
            and self._text[self._index + 1].lower() in JOTAWANYJA_LITARY
        ):
            converted_letter = soft
        elif (
            self._index < self._len - 2
            and self._text[self._index].lower()
            == self._text[self._index + 1].lower()
            == "л"
            and (
                self._text[self._index + 2].lower() in JOTAWANYJA_LITARY
                or self._text[self._index + 2].lower() == "ь"
            )
        ):
            converted_letter = soft
        elif (
            self._palatalization
            and self._index < self._len - 2
            and self._ci_patrabuje_adlustravannia_tranzityunaj_miakkasci()
        ):
            if self._text[self._index].lower() != "н" or (
                self._text[self._index].lower()
                == "н"
                == self._text[self._index + 1].lower()
            ):
                converted_letter = soft
            else:
                converted_letter = hard
        else:
            converted_letter = hard

        return converted_letter
