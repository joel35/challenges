import pytest

from workouts import print_workout_days


@pytest.mark.parametrize('test_input,expected', [('upper', 'Mon, Thu\n'),
                                                 ('lower', 'Tue, Fri\n'),
                                                 ('body', 'Mon, Tue, Thu, Fri\n'),
                                                 ('#1', 'Mon, Tue\n'),
                                                 ('#2', 'Thu, Fri\n'),
                                                 ('30', 'Wed\n'),
                                                 ('min', 'Wed\n'),
                                                 ('cardio', 'Wed\n'),
                                                 ('legs', 'No matching workout\n')])
def test_print_workout_days(capsys, test_input, expected):
    print_workout_days(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected

