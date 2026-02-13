"""Тэсты з сапраўднымі тэкстамі."""

# pylint: disable=non-ascii-name

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar

from tests.data.bahdanovicz import PRYKLAD_BAHDANOVICZ
from tests.data.kulaszou import KULASZOU_PRYKLAD


def test_z_pamylki():
    """Праверка канвертацыі тэкста з «Памылкі»."""
    assert (
        latynkatar.convert_latin(latynkatar.convert(KULASZOU_PRYKLAD, miakkasc=False))
        == KULASZOU_PRYKLAD
    )


def test_z_pamylki_stary():
    """Праверка канвертацыі тэкста з «Памылкі» да старога набора сімвалаў."""
    assert (
        latynkatar.convert_latin(
            latynkatar.convert_old(KULASZOU_PRYKLAD, miakkasc=False)
        )
        == KULASZOU_PRYKLAD
    )


def test_bahdanovicz():
    """Тэст на канвертацыю верша Багдановіча."""
    assert (
        latynkatar.convert_latin(
            latynkatar.convert(PRYKLAD_BAHDANOVICZ, miakkasc=False)
        )
        == PRYKLAD_BAHDANOVICZ
    )


def test_bahdanovicz_stary():
    """Тэст на канвертацыю верша Багдановіча да старога набора сімвалаў."""
    assert (
        latynkatar.convert_latin(
            latynkatar.convert_old(PRYKLAD_BAHDANOVICZ, miakkasc=False)
        )
        == PRYKLAD_BAHDANOVICZ
    )
