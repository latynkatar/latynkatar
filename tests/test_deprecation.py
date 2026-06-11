"""Тэсты на паведамленні аб запланаваным выдаленні функцый."""

import pytest

# Try to import from module, else import from the source code
try:
    import latynkatar
except ModuleNotFoundError:
    from src import latynkatar

FUNCTIONS = ["convert", "convert_latin", "convert_old"]


@pytest.mark.parametrize("function_name", FUNCTIONS)
def test_deprecation_warning(function_name: str):
    """Тэст на папярэджанне аб выдаленне функцый."""
    with pytest.warns() as captured_warning:
        getattr(latynkatar, function_name)("ыва")

        assert captured_warning[0].category is DeprecationWarning
        assert str(captured_warning[0].message) == (
            f"Using function/method '{function_name}()' is deprecated and will be removed in version '2.5.0': "
            "Канвертацыя функцыямі замененая непасрэдным доступам да класаў-канвертараў і будзе выдаленая."
        )
