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

from tests.data.bahdanovicz import (
    PRYKLAD_BAHDANOVICZ,
    UZOR_BAHDANOVICZ,
    UZOR_BAHDANOVICZ_STARY,
)
from tests.data.pamylka import PRYKLAD_PAMYLKA, UZOR_PAMYLKA, UZOR_PAMYLKA_STARY

_LOGGER = getLogger(__name__)
_CZAKANY_CZAS_NA_NOVUJU_ZIAMLU = 0.6 if os.getenv("CI") else 0.3


with open("tests/data/novaja_ziamla.txt", "r", encoding="utf-8") as novy_fail:
    NOVAJA_ZIAMLA = novy_fail.read()


def test_z_pamylki():
    """Праверка канвертацыі тэкста з «Памылкі»."""
    assert latynkatar.convert(PRYKLAD_PAMYLKA) == UZOR_PAMYLKA


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
    assert latynkatar.convert_old(PRYKLAD_PAMYLKA) == UZOR_PAMYLKA_STARY


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert latynkatar.convert(PRYKLAD_BAHDANOVICZ) == UZOR_BAHDANOVICZ


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert latynkatar.convert_old(PRYKLAD_BAHDANOVICZ) == UZOR_BAHDANOVICZ_STARY


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
