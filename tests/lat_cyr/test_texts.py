"""Тэсты з сапраўднымі тэкстамі."""

# pylint: disable=non-ascii-name

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar

from tests.data.bahdanovicz import BAHDANOVICZ_CYRRILIC
from tests.data.bahuszevicz import (
    VERABIEJ_I_KASZA_CYRRILIC,
    VIERABIEJ_I_KASZA_CZECH_LATIN,
    VIERABIEJ_I_KASZA_POLISH_LATIN,
)
from tests.data.kulaszou import KULASZOU


def test_z_pamylki():
    """Праверка канвертацыі верша Куляшова з сучаснай лацінкі."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(KULASZOU).convert(palatalization=False)
        ).convert()
        == KULASZOU
    )


def test_z_pamylki_stary():
    """Праверка канвертацыі верша Куляшова са старой лацінкі."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(KULASZOU).convert(
                palatalization=False, old_rules=True
            )
        ).convert()
        == KULASZOU
    )


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(BAHDANOVICZ_CYRRILIC).convert(
                palatalization=False
            )
        ).convert()
        == BAHDANOVICZ_CYRRILIC
    )


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча са старога набора сімвалаў."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(BAHDANOVICZ_CYRRILIC).convert(
                palatalization=False, old_rules=True
            )
        ).convert()
        == BAHDANOVICZ_CYRRILIC
    )


def test_verabiej_i_kasza():
    """Тэст на канвертацыю верша Багушэвіча."""
    assert (
        latynkatar.LatCyrConverter(VIERABIEJ_I_KASZA_CZECH_LATIN).convert()
        == VERABIEJ_I_KASZA_CYRRILIC
    )


def test_verabiej_i_kasza_stary():
    """Тэст на канвертацыю верша Багушэвіча да старой (польскай) лацінкі."""
    assert (
        latynkatar.LatCyrConverter(VIERABIEJ_I_KASZA_POLISH_LATIN).convert()
        == VERABIEJ_I_KASZA_CYRRILIC
    )
