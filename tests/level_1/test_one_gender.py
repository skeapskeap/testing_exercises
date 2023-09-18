import pytest

from functions.level_1.one_gender import genderalize


@pytest.mark.parametrize("verb_female", [None, "", "female_verb"])
@pytest.mark.parametrize("verb_male", [None, "", "male_verb"])
def test__genderalize__male(verb_male, verb_female):
    genderalized_verb = genderalize(verb_male=verb_male,
                                    verb_female=verb_female,
                                    gender="male")
    assert genderalized_verb == verb_male


@pytest.mark.parametrize("gender", [None, 0, 1, True, False, "any_string"])
@pytest.mark.parametrize("verb_female", [None, "", "female_verb"])
@pytest.mark.parametrize("verb_male", [None, "", "male_verb"])
def test__genderalize__female(verb_male, verb_female, gender):
    genderalized_verb = genderalize(verb_male=verb_male,
                                    verb_female=verb_female,
                                    gender=gender)
    assert genderalized_verb == verb_female
