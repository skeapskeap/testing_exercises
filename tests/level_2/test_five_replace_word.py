import pytest

from functions.level_2.five_replace_word import replace_word


@pytest.mark.parametrize("text", [
    pytest.param("one _word_ three", id="text lower case"),
    pytest.param("one _WORD_ three", id="text upper case"),
    pytest.param("one _WoRd_ three", id="text various case"),
])
@pytest.mark.parametrize("replace_from", [
    pytest.param("_word_", id="replace_from lower case"),
    pytest.param("_WORD_", id="replace_from upper case"),
    pytest.param("_wOrD_", id="replace_from various case"),
])
def test__replace_word__replace(text, replace_from):
    res = replace_word(text=text,
                       replace_from=replace_from,
                       replace_to="two")
    assert res == "one two three"
