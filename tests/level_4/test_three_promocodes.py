import pytest

from functions.level_4.three_promocodes import generate_promocode


def test__generate_promocode__call_with_defaults():
    promocode = generate_promocode()
    assert promocode.isalpha()
    assert promocode.isupper()
    assert len(promocode) == 8


@pytest.mark.parametrize("length, expected_promo_len", [
    pytest.param(-10, 0, id="negative len"),
    pytest.param(0, 0, id="zero len"),
    pytest.param(5, 5, id="positive len"),
])
def test__generate_promocode__specified_length(length: int, expected_promo_len):
    assert len(generate_promocode(length)) == expected_promo_len
