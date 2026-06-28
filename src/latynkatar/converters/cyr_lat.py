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
    CONSONANTS_WITH_PALATALIZATION_TRANSIT,
    CYR_TO_LAT_CONVERSION,
    CYRRILIC_ALPHABET,
    CYRRILIC_VOVELS,
    IOTATED_VOVELS,
    OLD_CYR_TO_LAT_CONVERSION,
    PALATIZEABLE_CONSONANTS,
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
        self._convertion_rules: dict[str, str]
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
        self._convertion_rules = (
            OLD_CYR_TO_LAT_CONVERSION if self._old_rules else CYR_TO_LAT_CONVERSION
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
            case letter if letter in self._convertion_rules:
                converted_letter = self._convertion_rules[lowercase_letter]
            case letter if letter in PALATIZEABLE_CONSONANTS:
                converted_letter = self.__convert_palatalized_consonants()
            case letter if letter in ["'", "ь"]:
                pass
            case letter if letter in IOTATED_VOVELS:
                converted_letter = self._convert_iotated()

        return self._letter_in_proper_register(converted_letter)

    def _letter_in_proper_register(self, converted_letter: str) -> str:
        proper_state = converted_letter
        if self._symbol.isupper():
            # Калі бягучая літара вялікая
            if (
                # Калі наступны сімвал таксама беларуская літара і гэтая ступрная літара вялікая
                self._next_symbol
                and self._next_symbol.lower() in CYRRILIC_ALPHABET
                and self._next_symbol.isupper()
            ) or (
                # Ці наступны сімвал гэта не літара або наступнага сімвала няма
                (
                    not self._next_symbol
                    or self._next_symbol.lower() not in CYRRILIC_ALPHABET
                )
                # І папярэдняя літара таксама вялікая
                and self._previos_letters
                and self._previos_letters[-1].isupper()
            ):
                # Тады ўсе лацінскія літары мусяць быць вялікімі
                proper_state = proper_state.upper()
            else:
                # Інакш толькі першая
                proper_state = proper_state.capitalize()

        return proper_state

    @property
    def _does_it_need_palatalization_transit(self) -> bool:
        """Правярае, ці патрабуе пазіцыя зычнай адлюстравання транзітыўнай мяккасці.

        :return: True, калі патрабуе
        :rtype: bool
        """
        return self._next_symbol.lower() in CONSONANTS_WITH_PALATALIZATION_TRANSIT and (
            self._second_next_symbol.lower() in IOTATED_VOVELS
            or self._second_next_symbol.lower() == "ь"
        )

    def _should_there_be_j(self) -> bool:
        """Спраўджае, ці патрэбная пры канвертацыі ётаваных j.

        :return: True, калі патрабуе
        :rtype: bool
        """
        return (
            not self._previos_letters
            or self._previos_letters[-1].lower() in CYRRILIC_VOVELS
            or self._previos_letters[-1].lower() in ("'", "ь", "ў")
        )

    def _convert_iotated(self) -> str:
        """Канвертуе ў лацінку літары з j/i: і, е, ё, ю, я.

        :return: Сканвертаваную да лацінкі літару. Вынікам часам можа быць некалькі літар.
        :rtype: str
        """
        if self._should_there_be_j() and self._symbol.lower() != "і":
            base = "j"
        else:
            base = "i"

        second_letter = IOTATED_VOVELS[self._symbol.lower()]
        if (
            self._symbol.lower() != "і"
            and self._previos_letters
            and self._previos_letters[-1].lower() == "л"
        ):
            base = ""

        converted_letter = base + second_letter

        return converted_letter

    def __convert_palatalized_consonants(self) -> str:
        """Канвертуе да лацінкі зычныя, якія могуць быць мяккімі.

        :return: Вынік канвертацыі
        :rtype: str
        """
        hard, soft = PALATIZEABLE_CONSONANTS[self._symbol.lower()]
        converted_letter = ""
        match True:
            case results if results == (self._next_symbol.lower() == "ь"):
                converted_letter = soft

            case results if results == (
                self._symbol.lower() == "л"
                and self._next_symbol.lower() in IOTATED_VOVELS
            ):
                converted_letter = soft
            case results if results == (
                self._symbol.lower() == self._next_symbol.lower() == "л"
                and (
                    self._second_next_symbol.lower() in IOTATED_VOVELS
                    or self._second_next_symbol.lower() == "ь"
                )
            ):
                converted_letter = soft
            case results if results == (
                self._palatalization
                and self._does_it_need_palatalization_transit
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
        return CYRRILIC_ALPHABET
