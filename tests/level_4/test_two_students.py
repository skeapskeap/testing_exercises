import pytest

from functions.level_4.two_students import get_student_by_tg_nickname, Student


def test__get_student_by_tg_nickname__returns_first_match(tg_user_name):
    students = [
        Student("Name", "Surname", f"@telegram_account"),
        Student("First", "Match", f"@{tg_user_name}"),
        Student("Second", "Match", f"@{tg_user_name}"),
    ]
    assert get_student_by_tg_nickname(tg_user_name, students) == students[1]


@pytest.mark.parametrize("telegram_account", ["@telegram_account", None])
def test__get_student_by_tg_nickname__returns_none_on_no_matches(tg_user_name, telegram_account):
    student = Student("Name", "Surname", telegram_account)
    assert get_student_by_tg_nickname(tg_user_name, [student]) is None


@pytest.mark.parametrize("wrong_account_format", [
    "{tg_user_name}",
    "{tg_user_name}@",
    "@{tg_user_name}@",
    "@@{tg_user_name}",
])
def test__get_student_by_tg_nickname__match_wrong_formatted_account(wrong_account_format, tg_user_name):
    student = Student("Name", "Surname", wrong_account_format.format(tg_user_name=tg_user_name))
    assert get_student_by_tg_nickname(tg_user_name, [student]) == student


@pytest.mark.parametrize("telegram_account", [
    pytest.param("@", id="telegram_account is '@'"),
    pytest.param("@@", id="telegram_account is '@@'"),
    pytest.param("@@@", id="telegram_account is '@@@'"),
])
def test__get_student_by_tg_nickname__many_at_match_to_empty_user(telegram_account: str):
    student = Student("Name", "Surname", telegram_account)
    assert get_student_by_tg_nickname(telegram_username="", students=[student]) == student
