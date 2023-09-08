from functions.level_1.four_bank_parser import parse_ineco_expense


def test_parse_ineco_expense(bank_test_case):

    expense = parse_ineco_expense(sms=bank_test_case.sms,
                                  cards=[bank_test_case.card])

    assert expense.amount == bank_test_case.expect_expense.amount
    assert expense.card == bank_test_case.expect_expense.card
    assert expense.spent_in == bank_test_case.expect_expense.spent_in
    assert expense.spent_at == bank_test_case.expect_expense.spent_at
