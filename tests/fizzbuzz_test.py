from src import fizzbuzz
import pytest


@pytest.mark.parametrize('n , result',[
    (1, '1'),
    (2, '2'),
    (3, 'Fizz'),
    (4, '4'),
    (5, 'Buzz'),
    (6, 'Fizz'),
    (7, '7'),
    (8, '8'),
    (9, 'Fizz'),
    (10, 'Buzz'),
    (11, '11'),
    (12, 'Fizz'),
    (13, '13'),
    (14, '14'),
    (15, 'FizzBuzz'),
])
def test_n_return_actual_value(n, result):
    actual_value = result
    assert actual_value == fizzbuzz(n)