import pytest

from functions.level_2.two_square_equation import solve_square_equation


@pytest.mark.parametrize("linear_coefficient_sign", [
    pytest.param(1, id="linear_coefficient_positive"),
    pytest.param(-1, id="linear_coefficient_negative"),
])
@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient", [
    (1, 1.99, 1),
    (2, 3.99, 2),
    (1, 3.99, 4),
    (1, 3.99, 4),
])
def test__solve_square_equation__negative_discriminant(square_coefficient,
                                                       linear_coefficient,
                                                       const_coefficient,
                                                       linear_coefficient_sign: int):
    res = solve_square_equation(
        square_coefficient,
        linear_coefficient * linear_coefficient_sign,
        const_coefficient
    )
    assert res == (None, None)


@pytest.mark.parametrize("linear_coefficient, const_coefficient, root_left, root_right", [
    (2, 3, -1.5, None),
    (2, -3, 1.5, None),
    (2, -3, 1.5, None),
    (-5, 10, 2, None),
    (-5, -10, -2, None),
])
def test__solve_square_equation__square_coefficient_eq_zero(linear_coefficient,
                                                            const_coefficient,
                                                            root_left,
                                                            root_right):
    root_left_, root_right_ = solve_square_equation(0, linear_coefficient, const_coefficient)
    assert root_left_ == root_left
    assert root_right_ == root_right


def test__solve_square_equation__square_and_linear_coefficients_eq_zero():
    assert solve_square_equation(0, 0, const_coefficient=123) == (None, None)


@pytest.mark.parametrize("square_coefficient, linear_coefficient, const_coefficient, root_left, root_right", [
    (1, 2, 1, -1.0, -1.0),
    (2, 4, 2, -1.0, -1.0),
    (1, 4, 4, -2.0, -2.0),
    (-1, 4, -4, 2.0, 2.0),
])
def test__solve_square_equation(square_coefficient,
                                linear_coefficient,
                                const_coefficient,
                                root_left,
                                root_right):
    root_left_, root_right_ = solve_square_equation(square_coefficient,
                                                    linear_coefficient,
                                                    const_coefficient)
    assert root_left_ == root_left
    assert root_right_ == root_right
