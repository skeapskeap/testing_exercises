import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize("gender, verb_male, verb_fem, expected",
                         [
                             ("male", "жил", "жила", "жил"),
                             ("female", "жил", "жила", "жила"),
                             ("other", "жил", "жила", "жила"),
                             (None, "жил", "жила", "жила"),
                         ])
def test_genderalize(gender, verb_male, verb_fem, expected):
    genderalized_verb = genderalize(verb_male=verb_male,
                                    verb_female=verb_fem,
                                    gender=gender)
    assert genderalized_verb == expected
