from gendiff.cli import parse_arguments
from gendiff.scripts.gendiff import generate_diff


def main():
    args = parse_arguments()
    try:
        result = generate_diff(args.first_file,
                               args.second_file)
        print(result)
    except Exception as error:
        print(error)


if __name__ == '__main__':
    main()
