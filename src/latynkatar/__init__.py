"""
Łatynkatar

    Маленькая і простая бібліятэка для канвертацыі кірыліцы ў сучасную (з ž, č, š і v,
    т.зв. "чэшскую") і старую(з ż, cz, sz і w, т.зв. "пользскую") лацінку.

Прыклады:
    >>> import latynkatar
    >>> # сучасная ("чэшская")
    >>> latynkatar.CyrLatConverter("Але лёс склаўся так, што хрусць і папалам!").convert(palatalization=True)
    'Ale los skłaŭsia tak, što chruść i papałam!'
    >>> # сучасная без пазначэння транзітыўнай мяккасці
    >>> latynkatar.CyrLatConverter("Але лёс склаўся так, што хрусць і папалам!").convert()
    'Ale los skłaŭsia tak, što chrusć i papałam!'
    >>> # старая ("польская")
    >>> latynkatar.CyrLatConverter(
            "Але лёс склаўся так, што хрусць і папалам!"
        ).convert(old_rules=True, palatalization=True)
    'Ale los skłaŭsia tak, szto chruść i papałam!'
    >>> # старая без пазначэння транзітыўнай мяккасці
    >>> latynkatar.CyrLatConverter("Але лёс склаўся так, што хрусць і папалам!").convert(old_rules=True)
    'Ale los skłaŭsia tak, szto chrusć i papałam!'
    >>> # канвертацыя лацініцы да кірыліцы
    >>> latynkatar.LatCyrConverter("Ale los skłaŭsia tak, što chrusć i papałam!").convert()
    'Але лёс склаўся так, што хрусць і папалам!'
    >>> latynkatar.LatCyrConverter("Ale los skłaŭsia tak, szto chrusć i papałam!").convert()
    'Але лёс склаўся так, што хрусць і папалам!'

Прынцыпы працы бібліятэкі:

    * Ніякага выпраўлення памылак.
    * Са зменаў правапісу толькі яўна пазначаецца транзітыўная мяккасць зычных, астатняе пры канвертацыі захоўваецца
    роўна з тымі ж асаблівасцямі правапісу і памылкамі, якія былі да канвертацыі. Прычым, пазначэнне мяккасці пры
    жаданні можна адключыць (гл. прыклад вышэй)
    * Усе словы разглядаюцца як раўназначныя. З улікам таго, што у лацінцы звычайна выкарыстоўваюцца арыгінальныя
    геаграфічныя назвы і імёны для моў, якія ўжываюць лацінскую графіку, вельмі раілі б вычытваць выніковы тэкст
    перад публікацыяй.
    * Кірылічныя сімвалы, якім адпавядае некалькі лацінскіх сімвалаў пры трансляцыі вялікіх літар маюць вялікай
    толькі першую літару ў пары (Chleb, Jan), што можа быць праблемай у выпадках, калі гэта не слова з вялікай
    літары ці абрэвіятура, а проста нешта напісанае КАПСАМ. Бо атрымаецца ChLEB, JaN.
    * Канвертацыя ў кірыліцу не змяняе ў арыгінальным тэксце нічога, так што ўсё заўвагі вышай тычацца і яе.
    Бібліятэка можа апрацоўваць тэкст, у каторым адначасова ўжываюцца "польскі" і "чэшскі" варыянты:


    >>> latynkatar.LatCyrConverter("Sztości dzieści šumić").convert()
    'Штосьці дзесьці шуміць'

    Больш падрабязна можна пачытаць у свежай версіі даведкі https://github.com/latynkatar/latynkatar/blob/main/README.md

    У якасці ўзору ўжывання бібліятэкі ці анлайн канвертара створанага на яе аснове магу
    прапанаваць паглядзець на сайт latynkatar.org.

Ліцэнзія

    This file is part of Łatynkatar.

    Latynkatar is free software: you can redistribute it and/or modify it under the
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

from .converters import CyrLatConverter, LatCyrConverter
from .latynkatar import convert, convert_latin, convert_old

__all__ = [
    "convert",
    "convert_old",
    "convert_latin",
    "CyrLatConverter",
    "LatCyrConverter",
]
