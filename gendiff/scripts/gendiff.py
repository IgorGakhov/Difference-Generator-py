import json

DIFFLINE_TEMPLATE = '  {} {}: {}'


def get_data_from_json(json_file):
    file = json.load(json_file)
    for key in file:
        value = file.get(key)
        if type(value) is bool:
            file[key] = str(value).lower()
        if value is None:
            file[key] = 'null'

    return file


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file1, open(file_path2) as file2:
        file1 = get_data_from_json(file1)
        file2 = get_data_from_json(file2)

    keys_1, keys_2 = set(file1.keys()), set(file2.keys())
    removed_keys = keys_1 - keys_2
    added_keys = keys_2 - keys_1
    all_keys = sorted(keys_1 | keys_2)

    result = []
    for key in all_keys:

        if key in removed_keys:
            value = file1[key]
            status = '-'

        elif key in added_keys:
            value = file2[key]
            status = '+'

        elif file1[key] == file2[key]:
            value = file1[key]
            status = ' '

        else:
            value_old = file1[key]
            status_old = '-'
            value = file2[key]
            status = '+'
            result.append(DIFFLINE_TEMPLATE.format(status_old, key, value_old))

        result.append(DIFFLINE_TEMPLATE.format(status, key, value))

    return '{\n' + "\n".join(result) + '\n}'
