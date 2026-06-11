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
    BAHDANOVICZ_CYRRILIC,
    BAHDANOVICZ_CZECH_LATIN,
    BAHDANOVICZ_POLISH_LATIN,
)
from tests.data.pamylka import (
    PAMYLKA_CYRRILIC,
    PAMYLKA_CZECH_LATIN,
    PAMYLKA_POLISH_LATIN,
)

_LOGGER = getLogger(__name__)
_CZAKANY_CZAS_NA_NOVUJU_ZIAMLU = 0.8 if os.getenv("CI") else 0.6


with open("tests/data/novaja_ziamla.txt", "r", encoding="utf-8") as novy_fail:
    NOVAJA_ZIAMLA = novy_fail.read()


def test_z_pamylki():
    """Праверка канвертацыі тэкста з «Памылкі»."""
    assert (
        latynkatar.CyrLatConverter(PAMYLKA_CYRRILIC).convert(palatalization=True)
        == PAMYLKA_CZECH_LATIN
    )


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
    assert (
        latynkatar.CyrLatConverter(PAMYLKA_CYRRILIC).convert(
            old_rules=True, palatalization=True
        )
        == PAMYLKA_POLISH_LATIN
    )


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert (
        latynkatar.CyrLatConverter(BAHDANOVICZ_CYRRILIC).convert(palatalization=True)
        == BAHDANOVICZ_CZECH_LATIN
    )


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert (
        latynkatar.CyrLatConverter(BAHDANOVICZ_CYRRILIC).convert(
            old_rules=True, palatalization=True
        )
        == BAHDANOVICZ_POLISH_LATIN
    )


def test_novaj_ziamloju():
    """Тэст хуткасці канвертацыі з дапамогай «Новай зямлі»."""
    start = monotonic()
    _ = latynkatar.CyrLatConverter(NOVAJA_ZIAMLA).convert()
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
    _ = latynkatar.CyrLatConverter(NOVAJA_ZIAMLA).convert(old_rules=True)
    finish = monotonic()

    time_required = finish - start

    _LOGGER.info(
        "Time stats:\n\tTest started at: '%f'\n\tFinished at: '%f'\n\t Convertation time: '%f'",
        start,
        finish,
        time_required,
    )

    assert time_required < _CZAKANY_CZAS_NA_NOVUJU_ZIAMLU
