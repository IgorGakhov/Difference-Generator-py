import pytest


from gendiff.constructor.gendiff import generate_diff


FLAT_JSON1 = 'tests/fixtures/diff_requests/file1.json'
FLAT_JSON2 = 'tests/fixtures/diff_requests/file2.json'
FLAT_JSON3 = 'tests/fixtures/diff_requests/file3.json'
FLAT_YAML1 = 'tests/fixtures/diff_requests/file1.yaml'
FLAT_YAML2 = 'tests/fixtures/diff_requests/file2.yaml'
FLAT_YML1 = 'tests/fixtures/diff_requests/file1.yml'
FLAT_YML2 = 'tests/fixtures/diff_requests/file2.yml'

RESPONSE_STYLISH_FLAT = 'tests/fixtures/diff_responses/stylish_flat.txt'
RESPONSE_STYLISH_FLAT2 = 'tests/fixtures/diff_responses/stylish_flat2.txt'


@pytest.mark.parametrize('file1, file2, response_file_path', [
    (FLAT_JSON1, FLAT_JSON2, RESPONSE_STYLISH_FLAT),
    (FLAT_JSON2, FLAT_JSON3, RESPONSE_STYLISH_FLAT2),
    (FLAT_YAML1, FLAT_YAML2, RESPONSE_STYLISH_FLAT),
    (FLAT_YAML1, FLAT_YAML2, RESPONSE_STYLISH_FLAT)
])
def test_generate_diff(file1, file2, response_file_path):
    with open(response_file_path) as file:
        expected_result = file.read()
    assert expected_result == generate_diff(file1, file2)


@pytest.fixture
def value_error_txt():
    return '''Extension ".txt" is not supported.
Use JSON or YML/YAML format'''


def test_usupported_file_format(value_error_txt):
    with pytest.raises(ValueError) as pytest_error:
        generate_diff(RESPONSE_STYLISH_FLAT, RESPONSE_STYLISH_FLAT2)
    assert pytest_error.type == ValueError
    assert str(pytest_error.value) == value_error_txt
