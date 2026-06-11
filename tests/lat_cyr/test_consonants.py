"""Тэсты на зычныя літары."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_d():
    """Тэст на канвертацыю D"""
    assert latynkatar.LatCyrConverter("DadodUDŭDE").convert() == "ДадодУДўДЭ"


def test_miakkija():
    """Тест на канвертацыю зычных, якія могуць пазначацца як мяккія"""
    assert latynkatar.LatCyrConverter("LnŚźcsłŃZć").convert() == "ЛьнСьзьцслНьЗць"


def test_l():
    """Тэст на канвертацыю l"""
    assert (
        latynkatar.LatCyrConverter("nadumali LuŁiLijulje").convert()
        == "надумалі ЛюЛ'іЛіюлье"
    )
