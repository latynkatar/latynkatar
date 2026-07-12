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
        latynkatar.LatCyrConverter(
            "ŁaElAŁuLiLuLOlEl lLa nadumali LuŁjiLijulje"
        ).convert()
        == "ЛаЭлЯЛуЛіЛюЛЁлЕль льЛя надумалі ЛюЛ'іЛіюлье"
    )


def test_ch():
    """Тэст карнвертацыі Ch."""
    assert (
        latynkatar.LatCyrConverter("ChaChu CHYVAChchchchchch Chich").convert()
        == "ХаХу ХЫВАХххххх Хіх"
    )


def test_sz():
    """Тэст канвертацыі sz/š."""
    assert (
        latynkatar.LatCyrConverter("SzaszuSzyszszszszszszsz ŠašuŠyššššššš").convert()
        == "ШашуШышшшшшшш ШашуШышшшшшшш"
    )


def test_cz():
    """Тэст канвертацыі cz/č."""
    assert latynkatar.LatCyrConverter("czACzyCZU čAČyČU").convert() == "чАЧыЧУ чАЧыЧУ"


def test_ż():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ż/ž."""
    assert (
        latynkatar.LatCyrConverter("żUrAwInYŻeŻY žUrAvInYŽeŽY").convert()
        == "жУрАвІнЫЖэЖЫ жУрАвІнЫЖэЖЫ"
    )


def test_v():
    """Тэст канвертацыі v/w."""
    assert (
        latynkatar.LatCyrConverter("wojt i Wajawoda vojt i Vajavoda").convert()
        == "войт і Ваявода войт і Ваявода"
    )


def test_miakki_znak():
    """Тэст канвертацыі ў мяккі знак."""
    assert latynkatar.LatCyrConverter("ńmńść").convert() == "ньмньсьць"


def test_miakkasci():
    """Тэст на перадачу транзітыўнай мякасці."""
    assert latynkatar.LatCyrConverter(
        "śnieh śmiech pośpiech śviaty Valancin žadańni pustazielle snieh smiech pospiech sviaty Valancin "
        "žadanni pustazielle"
    ).convert() == (
        "сьнег сьмех посьпех сьвяты Валянцін жаданьні пустазельле снег смех поспех святы Валянцін жаданні "
        "пустазельле"
    )
