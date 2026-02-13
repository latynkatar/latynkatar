"""Тэсты на зычныя літары."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_d():
    """Тэст на канвертацыю D"""
    assert latynkatar.convert_latin("DadodUDŭDE") == "ДадодУДўДЭ"


def test_miakkija():
    """Тест на канвертацыю зычных, якія могуць пазначацца як мяккія"""
    assert latynkatar.convert_latin("LnŚźcsłŃZć") == "ЛьнСьзьцслНьЗць"


def test_l():
    """Тэст на канвертацыю l"""
    assert latynkatar.convert_latin("nadumali LuŁiLijulje") == "надумалі ЛюЛ'іЛіюлье"
