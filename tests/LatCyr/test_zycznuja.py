"""Тэсты на зычныя літары."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_d():
    """Тэст на канвертацыю D"""
    assert latynkatar.convert_latin("DadodUDŭDE") == "ДадодУДўДЭ"
