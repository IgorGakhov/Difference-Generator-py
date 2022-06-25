import pytest

from gendiff.scripts.gendiff import generate_diff


FLAT_JSON1 = 'tests/fixtures/diff_requests/file1.json'
FLAT_JSON2 = 'tests/fixtures/diff_requests/file2.json'

RESPONSE_JSON_FLAT = 'tests/fixtures/diff_responses/json_flat.txt'


@pytest.mark.parametrize('file1, file2, response_file_path', [
    (FLAT_JSON1, FLAT_JSON2, RESPONSE_JSON_FLAT)
])
def test_generate_diff(file1, file2, response_file_path):
    with open(response_file_path) as file:
        expected_result = file.read()
    assert expected_result == generate_diff(file1, file2)
