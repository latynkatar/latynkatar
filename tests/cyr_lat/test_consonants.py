"""Тэсты на зычныя літары."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_l():
    """Тэст канвертацыі да пары l/ł."""
    assert latynkatar.convert("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя") == "ŁaElAŁuLiLuLOlEl lLa"


def test_ch():
    """Тэст карнвертацыі х."""
    assert latynkatar.convert("ХаХу ХЫВАХххххх Хіх") == "ChaChu ChYVAChchchchchch Chich"


def test_sz():
    """Тэст канвертацыі ш да старога набора сімвалаў."""
    assert latynkatar.convert_old("ШашуШышшшшшшш") == "SzaszuSzyszszszszszszsz"


def test_š():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ш да новага набора сімвалаў."""
    assert latynkatar.convert("ШашуШышшшшшшш") == "ŠašuŠyššššššš"


def test_cz():
    """Тэст канвертацыі ч да старога набора сімвалаў."""
    assert latynkatar.convert_old("чАЧыЧУ") == "czACzyCzU"


def test_č():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ч да новага набора сімвалаў."""
    assert latynkatar.convert("чАЧыЧУ") == "čAČyČU"


def test_ż():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ж да старога набора сімвалаў."""
    assert latynkatar.convert_old("жУрАвІнЫЖэЖЫ") == "żUrAwInYŻeŻY"


def test_ž():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ж да новага набора сімвалаў."""
    assert latynkatar.convert("жУрАвІнЫЖэЖЫ") == "žUrAvInYŽeŽY"


def test_w():
    """Тэст канвертацыі в да старога набора сімвалаў."""
    assert latynkatar.convert_old("войт і Ваявода") == "wojt i Wajawoda"


def test_v():
    """Тэст канвертацыі в да новага набора сімвалаў."""
    assert latynkatar.convert("войт і Ваявода") == "vojt i Vajavoda"


def test_miakki_znak():
    """Тэст канвертацыі мяккага знака."""
    assert latynkatar.convert("Ьньмьньсьць") == "ńmńść"


def test_miakkasci():
    """Тэст на перадачу транзітыўнай мякасці."""
    assert (
        latynkatar.convert(
            "снег смех поспех святы Валянцін жаданні пустазелле", miakkasc=True
        )
        == "śnieh śmiech pośpiech śviaty Valancin žadańni pustazielle"
    )


def test_biez_miakkasci():
    """Тэст на канвертацыю без перадачы транзітыўнай мяккасці."""
    assert (
        latynkatar.convert(
            "снег смех поспех святы Валянцін жаданні пустазелле", miakkasc=False
        )
        == "snieh smiech pospiech sviaty Valancin žadanni pustazielle"
    )
