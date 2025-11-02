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

:copyright: (c) 2025 Łatynkatar group: https://github.com/latynkatar
"""

from ..const import (
    HALOSNYJA,
    JOTAWANYJA_LITARY,
    MOHUC_PAZNACZACCA_JAK_MIAKKIJA,
    ZYCZNYJA_Z_TRANZITAM,
)


#
# Праверкі
#
def _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(
    next_symbol: str, second_next_symbol: str
) -> bool:
    """Правярае, ці патрабуе пазіцыя зычнай адлюстравання транзітыўнай мяккасці.

    :param next_symbol: наступны сімвал у тэксце
    :type next_symbol: str
    :param second_next_symbol: сімвал праз адзін ад бягучага
    :type second_next_symbol: str
    :return: True, калі патрабуе
    :rtype: bool
    """
    return next_symbol.lower() in ZYCZNYJA_Z_TRANZITAM and (
        second_next_symbol.lower() in JOTAWANYJA_LITARY
        or second_next_symbol.lower() == "ь"
    )


def _ci_patrabuje_j(previos_letters: list[str]) -> bool:
    """Спраўджае, ці патрэбная пры канвертацыі ётаваных j.

    :param previos_letters: папярэднія літары слова
    :type previos_letters: list[str]
    :return: True, калі патрабуе
    :rtype: bool
    """
    return (
        not previos_letters
        or previos_letters[-1].lower() in HALOSNYJA
        or previos_letters[-1].lower() in ("'", "ь")
    )


#
# Канвертацыя літары
#
def kanvertavac_jotavanyja(simval: str, previos_letters: list[str]) -> str:
    """Канвертуе ў лацінку літары з j/i: і, е, ё, ю, я.

    :param simval: бягучая літара ў тэксце
    :type simval: str
    :param previos_letters: папярэдняя літара ў тэксце
    :type previos_letters: list[str]
    :return: Сканвертаваную да лацінкі літару. Вынікам часам можа быць некалькі літар.
    :rtype: str
    """
    if _ci_patrabuje_j(previos_letters) and simval.lower() != "і":
        base = "j"
    else:
        base = "i"

    second_letter = JOTAWANYJA_LITARY[simval.lower()]
    if simval.lower() != "і" and previos_letters and previos_letters[-1].lower() == "л":
        base = ""

    converted_letter = base + second_letter

    return converted_letter


def kanvertavac_miakkija_zycznyja(
    simval: str, nastupny_simval: str, druhi_nastupny: str, miakkasc: bool
) -> str:
    """Канвертуе да лацінкі зычныя, якія могуць быць мяккімі.

    :param simval: Бягучы сімвал у тэксце
    :type simval: str
    :param nastupny_simval: Наступны сімвал у тэксце
    :type nastupny_simval: str
    :param druhi_nastupny: Сімвал праз адзін ад бягучага ў тэксце
    :type druhi_nastupny: str
    :param miakkasc: Ці пазначаць транзіт мякксаці. Калі False, то пакіне у тым выглядзе
        як было ў кірілічным арыгінале.
    :type miakkasc: bool
    :return: Вынік канвертацыі
    :rtype: str
    """
    hard, soft = MOHUC_PAZNACZACCA_JAK_MIAKKIJA[simval.lower()]
    converted_letter = ""
    match True:
        case results if results == (nastupny_simval.lower() == "ь"):
            converted_letter = soft

        case results if results == (
            simval.lower() == "л" and nastupny_simval.lower() in JOTAWANYJA_LITARY
        ):
            converted_letter = soft
        case results if results == (
            simval.lower() == nastupny_simval.lower() == "л"
            and (
                druhi_nastupny.lower() in JOTAWANYJA_LITARY
                or druhi_nastupny.lower() == "ь"
            )
        ):
            converted_letter = soft
        case results if results == (
            miakkasc
            and _ci_patrabuje_adlustravannia_tranzityunaj_miakkasci(
                nastupny_simval, druhi_nastupny
            )
            and not (simval == "н" and nastupny_simval == "ц")
        ):
            converted_letter = soft
        case _:
            converted_letter = hard

    return converted_letter
