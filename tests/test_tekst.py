"""Тэсты з сапраўднымі тэкстамі."""

# pylint: disable=non-ascii-name
import os
from logging import getLogger
from time import monotonic

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


_LOGGER = getLogger(__name__)
_CZAKANY_CZAS_NA_NOVUJU_ZIAMLU = 0.6 if os.getenv("CI") else 0.3

# Узор узяты з часопіса PAMYŁKA:
# https://github.com/PAMYLKA-ZIN/pamylka-number-3/tree/main/PAMYLKA_ZIN_3_FOR_SHARING
PRYKŁAD_PAMYŁKA = """Вітаем цябе, чытачу!
Гэта трэці нумар PAMYŁKA ZIN!
Мы вельмі цешымся, што да каманды стваральнікаў працягваюць далучацца
новыя навукоўцы і мастакі! І мы будзем радыя кожнаму новаму ўдзельніку!
Сябры, мы рэдакцыяй надумалі запачаткаваць прэмію – «Бізон Гіґс». Таму гэты
нумар мы прысвячаем усім беларускім навукоўцам і хочам анансаваць прэмію,
якая будзе ўвасабляць сабой Беларусь і навуку разам! Гэта ўзнагарода для
беларускіх навукоўцаў і даследнікаў дакладных і прыродазнаўчых навук ад
навукова-папулярнага часопісу Pamyłka Zin.
Больш дэталяў апавядае першы артыкул нумару.
"""
UZOR_PAMYŁKA = """Vitajem ciabie, čytaču!
Heta treci numar PAMYŁKA ZIN!
My vielmi ciešymsia, što da kamandy stvaralnikaŭ praciahvajuć dałučacca
novyja navukoŭcy i mastaki! I my budziem radyja kožnamu novamu ŭdzielniku!
Siabry, my redakcyjaj nadumali zapačatkavać premiju – «Bizon Higs». Tamu hety
numar my pryśviačajem usim biełaruskim navukoŭcam i chočam anansavać premiju,
jakaja budzie ŭvasablać saboj Biełaruś i navuku razam! Heta ŭznaharoda dla
biełaruskich navukoŭcaŭ i daślednikaŭ dakładnych i pryrodaznaŭčych navuk ad
navukova-papularnaha časopisu Pamyłka Zin.
Bolš detalaŭ apaviadaje pieršy artykuł numaru.
"""
UZOR_PAMYŁKA_STARY = """Witajem ciabie, czytaczu!
Heta treci numar PAMYŁKA ZIN!
My wielmi cieszymsia, szto da kamandy stwaralnikaŭ praciahwajuć dałuczacca
nowyja nawukoŭcy i mastaki! I my budziem radyja kożnamu nowamu ŭdzielniku!
Siabry, my redakcyjaj nadumali zapaczatkawać premiju – «Bizon Higs». Tamu hety
numar my pryświaczajem usim biełaruskim nawukoŭcam i choczam anansawać premiju,
jakaja budzie ŭwasablać saboj Biełaruś i nawuku razam! Heta ŭznaharoda dla
biełaruskich nawukoŭcaŭ i daślednikaŭ dakładnych i pryrodaznaŭczych nawuk ad
nawukowa-papularnaha czasopisu Pamyłka Zin.
Bolsz detalaŭ apawiadaje pierszy artykuł numaru.
"""

PRYKŁAD_BAHDANOVIČ = """Маладыя гады,
Маладыя жаданні!
Ні жуды, ні нуды,
Толькі шчасьце каханьня!

Помніш толькі красу,
Мілы тварык дзявочы,
Залатую касу,
Сіняватыя вочы!

Цёмны сад-вінаград,
Цьвет бяленькі вішнёвы, —
І агністы пагляд,
І гарачыя словы!

Будзь жа, век малады,
Поўны сьветлымі днямі!
Пралятайце, гады,
Залатымі агнямі!
"""
UZOR_BAHDANOVIČ = """Maładyja hady,
Maładyja žadańni!
Ni žudy, ni nudy,
Tolki ščaście kachańnia!

Pomniš tolki krasu,
Miły tvaryk dziavočy,
Załatuju kasu,
Siniavatyja vočy!

Ciomny sad-vinahrad,
Ćviet bialeńki višniovy, —
I ahnisty pahlad,
I haračyja słovy!

Budź ža, viek małady,
Poŭny śvietłymi dniami!
Pralatajcie, hady,
Załatymi ahniami!
"""
UZOR_BAHDANOVIČ_STARY = """Maładyja hady,
Maładyja żadańni!
Ni żudy, ni nudy,
Tolki szczaście kachańnia!

Pomnisz tolki krasu,
Miły twaryk dziawoczy,
Załatuju kasu,
Siniawatyja woczy!

Ciomny sad-winahrad,
Ćwiet bialeńki wiszniowy, —
I ahnisty pahlad,
I haraczyja słowy!

Budź ża, wiek małady,
Poŭny świetłymi dniami!
Pralatajcie, hady,
Załatymi ahniami!
"""

with open("tests/data/novaja_ziamla.txt", "r", encoding="utf-8") as novy_fail:
    NOVAJA_ZIAMLA = novy_fail.read()


def test_z_pamylki():
    """Праверка канвертацыі тэкста з «Памылкі»."""
    assert latynkatar.convert(PRYKŁAD_PAMYŁKA) == UZOR_PAMYŁKA


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
    assert latynkatar.convert_old(PRYKŁAD_PAMYŁKA) == UZOR_PAMYŁKA_STARY


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert latynkatar.convert(PRYKŁAD_BAHDANOVIČ) == UZOR_BAHDANOVIČ


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert latynkatar.convert_old(PRYKŁAD_BAHDANOVIČ) == UZOR_BAHDANOVIČ_STARY


def test_novaj_ziamloju():
    """Тэст хуткасці канвертацыі з дапамогай «Новай зямлі»."""
    start = monotonic()
    _ = latynkatar.convert(NOVAJA_ZIAMLA)
    finish = monotonic()

    time_required = finish - start

    _LOGGER.info(
        "Time stats:\n\tTest started at: '%f'\n\tFinished at: '%f'\n\t Convertation time: '%f'",
        start,
        finish,
        time_required,
    )

    assert time_required < _CZAKANY_CZAS_NA_NOVUJU_ZIAMLU


def test_novaj_ziamloju_stary():
    """Тэст хуткасці канвертацыі з дапамогай «Новай зямлі» (стары набор сімвалаў)."""
    start = monotonic()
    _ = latynkatar.convert_old(NOVAJA_ZIAMLA)
    finish = monotonic()

    time_required = finish - start

    _LOGGER.info(
        "Time stats:\n\tTest started at: '%f'\n\tFinished at: '%f'\n\t Convertation time: '%f'",
        start,
        finish,
        time_required,
    )

    assert time_required < _CZAKANY_CZAS_NA_NOVUJU_ZIAMLU
