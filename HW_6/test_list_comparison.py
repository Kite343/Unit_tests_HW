# Name                      Stmts   Miss  Cover
# ---------------------------------------------
# list_comparison.py           24      0   100%
# test_list_comparison.py      20      0   100%
# ---------------------------------------------
# TOTAL                        44      0   100%

import pytest

from list_comparison import ListComparison

# проверка правильности подсчета
@pytest.mark.parametrize('a, b, result', [
    ([7, 9, 5], [], (7, 0.0)),
    ([], [6, 3, 4, 7, 11], (0.0, 6.2)),
])
def test_get_average_lists(a, b, result):
    test_list_comparison = ListComparison(a, b)
    assert test_list_comparison.get_average_lists() == result, 'get_average_lists failed, incorrect counting result'

# запуск тестов с разными параметрами:
# среднее значение первого спика больше
# среднее значение второго спика больше
# средние знаения равны
# передача пустых списков
@pytest.mark.parametrize('a, b, result', [
    ([1, 4, 7], [4, 2], "Первый список имеет большее среднее значение"),
    ([3, 2], [1, 4, 7, 9], "Второй список имеет большее среднее значение"),
    ([4, 7, 9], [7, 9, 4], "Средние значения равны"),
    ([], [], "Средние значения равны"),
    ([8, 9, 7], [], "Первый список имеет большее среднее значение"),
    ([], [4, 8, 9], "Второй список имеет большее среднее значение"),
    ([1, 4, 7], [-1, -4, -7], "Первый список имеет большее среднее значение"),
    ([-3, -2], [3, 2], "Второй список имеет большее среднее значение"),
    ([], [-90, -4, -7], "Первый список имеет большее среднее значение"),
    ([-36, -2], [], "Второй список имеет большее среднее значение"),
    ])
def test_param(a, b, result):
    test_list_comparison = ListComparison(a, b)
    assert test_list_comparison.list_comparison() == result, 'test_param failed'

# проверка передаваемых значений на ошибку типа (передается не list)
@pytest.mark.parametrize('a, b', [
    (1, [7, 8]),
    ("a", [8, 9]),
    ([5, 7], 8),
    ([], "i")
    ])
def test_TypeError(a, b):
    with pytest.raises(TypeError):
        test_list_comparison = ListComparison(a, b)

# проверка передаваемых значений на ошибку значения
# списки содержат не только числа
@pytest.mark.parametrize('a, b', [
    ([6, 8, "7"], [7, 8]),
    ([7, 9, "a", 8], []),
    ([], [8, 77, "6", 89]),
    ([7, 65], ["i"]),
    ([[9, 8], 9, 8], [6, 4, 1]),
    ([8, 6, 5, 0], [7, 4, (1, 2, 7), 11])
    ])
def test_ValueError(a, b):
    with pytest.raises(ValueError):
        test_list_comparison = ListComparison(a, b)


if __name__ == '__main__':
    # ['-v'] - для подробных выводов
    pytest.main(['-v'])

# coverage run -m test_list_comparison -v
# coverage report

# Name                      Stmts   Miss  Cover
# ---------------------------------------------
# list_comparison.py           24      0   100%
# test_list_comparison.py      20      0   100%
# ---------------------------------------------
# TOTAL                        44      0   100%