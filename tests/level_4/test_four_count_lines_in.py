from functions.level_4.four_lines_counter import count_lines_in


def test__count_lines_in_count_valid_lines(create_test_file):
    lines = [f"row_{i}" for i in range(10)]
    file_name = create_test_file(content="\n".join(lines))
    assert count_lines_in(filepath=file_name) == len(lines)


def test__count_lines_in__doesnt_count_commented_lines(create_test_file):
    lines = [f"row_{i}" for i in range(10)]
    commented_lines = [f"#row_{i}" for i in range(5)]
    file_name = create_test_file(content="\n".join(lines + commented_lines))
    assert count_lines_in(filepath=file_name) == len(lines)


def test__count_lines_in__ignore_whitespaces_before_hashtag(create_test_file):
    commented_lines = [f" #row_{i}" for i in range(5)]
    file_name = create_test_file(content="\n".join(commented_lines))
    assert count_lines_in(filepath=file_name) == 0


def test__count_lines_in__file_doesnt_exist(uuid_filename):
    assert count_lines_in(filepath=uuid_filename) is None


def test__count_lines_in__filepath_is_dir(create_test_dir):
    uuid_filename = create_test_dir()
    assert count_lines_in(filepath=uuid_filename) is None
