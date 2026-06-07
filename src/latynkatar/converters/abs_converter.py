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

from __future__ import annotations

from abc import ABC, abstractmethod


class AbstractConverter(ABC):  # pylint: disable=too-few-public-methods
    """Абстрактная класа-канвертар, на якой мусяць будавацца ўсе астатнія канвертары."""

    @abstractmethod
    def __init__(self) -> None:
        self._index: int
        self._text: str
        self._len: int
        self._in_word_now: bool
        self._previos_letters: list[str]
        raise NotImplementedError

    def convert(self) -> str:
        """Канвертуе тэкст.

        :return: Сканвертаваны тэкст
        :rtype: str
        """
        converted_text = ""

        self._index = 0
        while self._index < len(self._text):
            if self._text[self._index].lower() in self._current_alphabet:
                self._in_word_now = True
                converted_text += self._convert_letter()
                self._previos_letters.append(self._text[self._index])
            else:
                self._in_word_now = False
                converted_text += self._text[self._index]
                self._previos_letters = []
            self._index += 1
        return converted_text

    @abstractmethod
    def _convert_letter(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def _current_alphabet(self) -> list[str]:
        raise NotImplementedError

    @property
    @abstractmethod
    def _symbol(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def _next_symbol(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def _second_next_symbol(self) -> str:
        raise NotImplementedError
