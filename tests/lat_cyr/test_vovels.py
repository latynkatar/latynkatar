"""Тэсты на канвертацыю галосных."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_ju():
    """Тэст на канвертацыю да ю"""
    assert (
        latynkatar.LatCyrConverter("JurliViec lUbiĆ lIju pju").convert()
        == "ЮрліВец лЮбіЦь лІю п'ю"
    )


def test_ja():
    """Тэст на канвертацыю да я"""
    assert (
        latynkatar.LatCyrConverter("JazjavaZIapaźiaVA").convert() == "Яз'яваЗЯпазьяВА"
    )


def test_jotavanyja_pa_u_nieskladovyn():
    """Тест на канвертацыю ётаваных па ў."""
    assert latynkatar.LatCyrConverter("zdaroŭje ŠČAŬJA").convert() == "здароўе ШЧАЎЯ"


def test_i_pa_apostrafe():
    """Тэст на напісанне і пасля апострафа."""
    assert (
        latynkatar.LatCyrConverter("padvorji vierabji vierabjiny").convert()
        == "падвор'і вераб'і вераб'іны"
    )


def test_vialikija_litary():
    """Тест на розныя спалучэнні вялікіх і малых літар."""
    assert (
        latynkatar.LatCyrConverter(
            "Chleb dzień MIASA RYBA I Jo Svajaki SMIATANA CHLEB JEVA JAN"
        ).convert()
        == "Хлеб дзень МЯСА РЫБА І Ё Сваякі СМЯТАНА ХЛЕБ ЕВА ЯН"
    )
