"""Тэсты з сапраўднымі тэкстамі."""

# pylint: disable=non-ascii-name

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar

from tests.data.bahdanovicz import BAHDANOVICZ_CYRRILIC
from tests.data.kulaszou import KULASZOU


def test_z_pamylki():
    """Праверка канвертацыі тэкста з «Памылкі»."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(KULASZOU).convert(palatalization=False)
        ).convert()
        == KULASZOU
    )


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
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
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert (
        latynkatar.LatCyrConverter(
            latynkatar.CyrLatConverter(BAHDANOVICZ_CYRRILIC).convert(
                palatalization=False, old_rules=True
            )
        ).convert()
        == BAHDANOVICZ_CYRRILIC
    )
