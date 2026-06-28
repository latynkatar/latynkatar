"""Тэсты на канвертацыю галосных."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_ju():
    """Тэст на канвертацыю ю"""
    assert (
        latynkatar.CyrLatConverter("ЮрліВец лЮбіЦь лІю п'ю").convert(
            palatalization=True
        )
        == "JurliViec lUbiĆ lIju pju"
    )


def test_ja():
    """Тэст на канвертацыю я"""
    assert (
        latynkatar.CyrLatConverter("Яз'яваЗЯпазЬяВА").convert(palatalization=True)
        == "JazjavaZIapaźjaVA"
    )


def test_jotavanyja_pa_u_nieskladovyn():
    """Тест на канвертацыю ётаваных па ў."""
    assert latynkatar.CyrLatConverter("здароўе ШЧАЎЯ").convert() == "zdaroŭje ŠČAŬJA"


def test_i_pa_apostrafe():
    """Тэст на напісанне і пасля апострафа."""
    assert (
        latynkatar.CyrLatConverter("падвор'і вераб'і").convert() == "padvorji vierabji"
    )


def test_vialikija_litary():
    """Тест на розныя спалучэнні вялікіх і малых літар."""
    assert (
        latynkatar.CyrLatConverter(
            "Хлеб дзень МЯСА РЫБА І Ё Сваякі СМЯТАНА ХЛЕБ ЕВА ЯН"
        ).convert()
        == "Chleb dzień MIASA RYBA I Jo Svajaki SMIATANA CHLEB JEVA JAN"
    )
