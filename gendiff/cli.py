import argparse


from gendiff.constants import FORMATS, DEFAULT_FORMAT


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format',
                        help='set format of output (default: stylish)',
                        choices=FORMATS,
                        default=DEFAULT_FORMAT
                        )

    args = parser.parse_args()

    return args
