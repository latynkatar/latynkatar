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
        latynkatar.convert_latin(latynkatar.convert(KULASZOU, miakkasc=False))
        == KULASZOU
    )


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
    assert (
        latynkatar.convert_latin(latynkatar.convert_old(KULASZOU, miakkasc=False))
        == KULASZOU
    )


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert (
        latynkatar.convert_latin(
            latynkatar.convert(BAHDANOVICZ_CYRRILIC, miakkasc=False)
        )
        == BAHDANOVICZ_CYRRILIC
    )


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert (
        latynkatar.convert_latin(
            latynkatar.convert_old(BAHDANOVICZ_CYRRILIC, miakkasc=False)
        )
        == BAHDANOVICZ_CYRRILIC
    )
