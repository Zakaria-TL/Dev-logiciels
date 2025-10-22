import pytest


@pytest.mark.parametrize('n , result',[
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
])
def test_n_return_actual_value(n, result):
    actual_value = result
    assert actual_value == fizzbuzz(n)