import pytest
import string
from tasks.Lesson_2 import generate_random_dicts, aggregate_dicts


def test_generate_random_dicts():
    dict_list = generate_random_dicts()
    assert isinstance(dict_list, list)
    assert 2 <= len(dict_list) <= 10
    for dictionary in dict_list:
        assert isinstance(dictionary, dict)
        assert 1 <= len(dictionary) <= 6
        for key, value in dictionary.items():
            assert key in string.ascii_letters
            assert 0 <= value <= 100


@pytest.mark.parametrize("dict_list, expected_result", [
    (
        [{'a': 10, 'b': 20}, {'a': 15, 'c': 30}, {'b': 25, 'd': 40}],
        {'a_2': 15, 'b_3': 25, 'c': 30, 'd': 40}
    ),
    (
        [{'x': 5}, {'x': 10}, {'y': 20}],
        {'x_2': 10, 'y': 20}
    ),
    (
        [],
        {}
    ),
    (
        [{}, {}, {}, {}],
        {}
    )
])
def test_aggregate_dicts(dict_list, expected_result):
    result_dict = aggregate_dicts(dict_list)
    assert result_dict == expected_result


@pytest.mark.parametrize("invalid_input", [
    00000,
    'string',
    {1: 'value'},
    [1, 'string1', 45, 'string2'],
    [{"a": 10}, '{\'b\': 30}', {"b": 30}],
    [{10: 10, 20: 20}],
    [{'a': '10', 'b': '20'}],
])
def test_aggregate_dicts_exceptions(invalid_input):
    with pytest.raises(TypeError):
        aggregate_dicts(invalid_input)


if __name__ == "__main__":
    pytest.main()