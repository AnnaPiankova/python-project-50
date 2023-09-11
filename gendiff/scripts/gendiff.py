#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.tools.argparse import parse_arg


def main():
    path_file1, path_file2, format_name = parse_arg()
    result = generate_diff(path_file1, path_file2)
    print(result)


if __name__ == '__main__':
    main()