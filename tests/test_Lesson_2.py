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


def test_aggregate_dicts():
    dict_list = [
        {'a': 10, 'b': 20},
        {'a': 15, 'c': 30},
        {'b': 25, 'd': 40}
    ]
    result_dict = aggregate_dicts(dict_list)
    expected_result = {
        'a_2': 15,
        'b_3': 25,
        'c': 30,
        'd': 40
    }
    assert result_dict == expected_result

    dict_list = [
        {'x': 5},
        {'x': 10},
        {'y': 20}
    ]
    result_dict = aggregate_dicts(dict_list)
    expected_result = {
        'x_2': 10,
        'y': 20
    }
    assert result_dict == expected_result


# Test aggregate_dicts function when the list is empty
def test_aggregate_dicts_empty_list():
    dict_list = []
    result_dict = aggregate_dicts(dict_list)
    expected_result = {}
    assert result_dict == expected_result

# Test all dictionaries are empty
def test_aggregate_dicts_all_empty_dicts():
    dict_list = [{}, {}, {}, {}]
    result_dict = aggregate_dicts(dict_list)
    expected_result = {}
    assert result_dict == expected_result

# Test all dictionaries are the same
def test_aggregate_dicts_all_same_dicts():
    dict_list = [{'a': 10, 'b': 20}, {'a': 10, 'b': 20}, {'a': 10, 'b': 20}]
    result_dict = aggregate_dicts(dict_list)
    expected_result = {
        'a_1': 10,
        'b_1': 20
    }
    assert result_dict == expected_result


if __name__ == "__main__":
    pytest.main()