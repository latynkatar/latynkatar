"""Тэсты на канвертацыю галосных."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_ju():
    """Тэст на канвертацыю ю"""
    assert latynkatar.convert("ЮрліВец лЮбіЦь лІю п'ю") == "JurliViec lUbiĆ lIju pju"


def test_ja():
    """Тэст на канвертацыю я"""
    assert latynkatar.convert("Яз'яваЗЯпазЬяВА") == "JazjavaZIapaźjaVA"
