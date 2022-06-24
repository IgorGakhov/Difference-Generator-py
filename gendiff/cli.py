import argparse

from gendiff.engine.gendiff import generate_diff


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    parse_arguments()
