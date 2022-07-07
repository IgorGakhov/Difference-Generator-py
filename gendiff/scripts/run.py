# !usr/bin/env python3

from gendiff.cli import parse_arguments
from gendiff.constructor.gendiff import generate_diff


def main() -> str:
    """
    Description:
    ---
        Program entry point.

    Return:
    ---
        Output the result of the generate_diff() function.
    """
    args = parse_arguments()
    try:
        result = generate_diff(args.first_file,
                               args.second_file,
                               args.format
                               )
        print(result)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
