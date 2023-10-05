import pytest

from functions.level_4.five_extra_fields import fetch_app_config_field
from functions.level_4.five_extra_fields import fetch_extra_fields_configuration


def test__fetch_app_config_field__returns_none_if_file_doesnt_exist(uuid_filename):
    assert fetch_app_config_field(uuid_filename, "field_name") is None


def test__fetch_app_config_field__returns_none_if_no_proper_section(create_test_file):
    config = "[not_proper_section] \nexpected_field: 123"
    config_file_name = create_test_file(content=config)
    assert fetch_app_config_field(config_file_name, "expected_field") is None


def test__fetch_app_config_field__returns_none_if_no_field(create_test_file):
    config = "[tool:app-config] \nnot_expected_field: 123"
    config_file_name = create_test_file(content=config)
    assert fetch_app_config_field(config_file_name, "expected_field") is None


def test__fetch_app_config_field__returns_field_value(create_test_file):
    field_name = "field_name"
    field_value = "field_value"
    config = f"[tool:app-config] \n{field_name}: {field_value}"
    config_file_name = create_test_file(content=config)

    assert fetch_app_config_field(config_file_name, field_name) == field_value


def test__fetch_extra_fields_configuration(create_test_file):
    config = f"[tool:app-config] \nextra_fields: \n f1: 2 * 2 \n f2: 2"
    expected = {"f1": 4, "f2": 2}
    config_file_name = create_test_file(content=config)

    assert fetch_extra_fields_configuration(config_file_name) == expected


@pytest.mark.parametrize("delimiter", [
    pytest.param("= ", id="equal sign as delimiter"),
    pytest.param(":", id="no space after semicolon"),
])
def test__fetch_extra_fields_configuration__raises_with_alt_delimiters(create_test_file, delimiter):
    config = f"[tool:app-config] \nextra_fields: \n f1{delimiter}1 \n f2{delimiter}2"
    config_file_name = create_test_file(content=config)

    with pytest.raises(IndexError):
        fetch_extra_fields_configuration(config_file_name)


def test__fetch_extra_fields_configuration__returns_empty_dict_if_no_extra_fields(create_test_file):
    config = f"[tool:app-config] \nnot_extra_fields: \n f1: 1 \n f2: 2"
    config_file_name = create_test_file(content=config)

    assert fetch_extra_fields_configuration(config_file_name) == {}
