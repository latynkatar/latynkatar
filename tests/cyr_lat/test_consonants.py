"""Тэсты на зычныя літары."""

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar


def test_l():
    """Тэст канвертацыі да пары l/ł."""
    assert (
        latynkatar.CyrLatConverter("ЛаЭлЯЛуЛіЛюЛЁлЕлЬ лЛя").convert()
        == "ŁaElAŁuLiLuLOlEl lLa"
    )


def test_ch():
    """Тэст карнвертацыі х."""
    assert (
        latynkatar.CyrLatConverter("ХаХу ХЫВАХххххх Хіх").convert()
        == "ChaChu ChYVAChchchchchch Chich"
    )


def test_sz():
    """Тэст канвертацыі ш да старога набора сімвалаў."""
    assert (
        latynkatar.CyrLatConverter("ШашуШышшшшшшш").convert(old_rules=True)
        == "SzaszuSzyszszszszszszsz"
    )


def test_š():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ш да новага набора сімвалаў."""
    assert latynkatar.CyrLatConverter("ШашуШышшшшшшш").convert() == "ŠašuŠyššššššš"


def test_cz():
    """Тэст канвертацыі ч да старога набора сімвалаў."""
    assert latynkatar.CyrLatConverter("чАЧыЧУ").convert(old_rules=True) == "czACzyCzU"


def test_č():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ч да новага набора сімвалаў."""
    assert latynkatar.CyrLatConverter("чАЧыЧУ").convert() == "čAČyČU"


def test_ż():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ж да старога набора сімвалаў."""
    assert (
        latynkatar.CyrLatConverter("жУрАвІнЫЖэЖЫ").convert(old_rules=True)
        == "żUrAwInYŻeŻY"
    )


def test_ž():  # pylint: disable=non-ascii-name
    """Тэст канвертацыі ж да новага набора сімвалаў."""
    assert latynkatar.CyrLatConverter("жУрАвІнЫЖэЖЫ").convert() == "žUrAvInYŽeŽY"


def test_w():
    """Тэст канвертацыі в да старога набора сімвалаў."""
    assert (
        latynkatar.CyrLatConverter("войт і Ваявода").convert(old_rules=True)
        == "wojt i Wajawoda"
    )


def test_v():
    """Тэст канвертацыі в да новага набора сімвалаў."""
    assert latynkatar.CyrLatConverter("войт і Ваявода").convert() == "vojt i Vajavoda"


def test_miakki_znak():
    """Тэст канвертацыі мяккага знака."""
    assert latynkatar.CyrLatConverter("Ьньмьньсьць").convert() == "ńmńść"


def test_miakkasci():
    """Тэст на перадачу транзітыўнай мякасці."""
    assert (
        latynkatar.CyrLatConverter(
            "снег смех поспех святы Валянцін жаданні пустазелле"
        ).convert(palatalization=True)
        == "śnieh śmiech pośpiech śviaty Valancin žadańni pustazielle"
    )


def test_biez_miakkasci():
    """Тэст на канвертацыю без перадачы транзітыўнай мяккасці."""
    assert (
        latynkatar.CyrLatConverter(
            "снег смех поспех святы Валянцін жаданні пустазелле"
        ).convert()
        == "snieh smiech pospiech sviaty Valancin žadanni pustazielle"
    )
