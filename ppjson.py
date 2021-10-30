"""
Pretty print and save JSON files
"""
import json
import argparse
from pathlib import Path
from os import sep


def ppjson(directory, jsonfiles, indent):
    """
    pretty print and save the list of json files
    """
    basedir = Path(directory)
    assert basedir.exists(), '{} does not exist'.format(directory)
    for each_file in jsonfiles:
        each_path = basedir / each_file
        each_pp_path = basedir / f'pp_{each_file}'
        if each_path.exists():
            with open(each_path) as jf:
                jsonobj = json.load(jf)
            with open(each_pp_path, 'w') as ppjf:
                json.dump(jsonobj, ppjf, indent=indent)
            print(f'Pretty printed JSON is saved here: {each_pp_path}')
        else:
            print(f'{each_path} does not exist, skip pretty print this file')


def get_args():
    """
    Get arguments from shell
    """
    parser = argparse.ArgumentParser(description='Pretty print JSON files')
    parser.add_argument(
        '-d', '--directory', default='.', nargs='+',
        help='absolute/relative directory to the json files'
    )
    parser.add_argument(
        '-f', '--jsonfiles', nargs='+', required=True,
        help='list of file names separated by space'
    )
    parser.add_argument(
        '-i', '--indent', type=int, default=4,
        help='JSON array elements and object members will be pretty-printed with this indent level'
    )
    return parser.parse_args()


if __name__ == "__main__":
    ARGS = get_args()
    ARGS.directory = ' '.join(ARGS.directory)
    ARGS.directory = ARGS.directory.rstrip(sep)
    ARGS.directory = ARGS.directory.rstrip('"')  # Path ending with a single '\' may produce '"'

    ppjson(directory=ARGS.directory, jsonfiles=ARGS.jsonfiles, indent=ARGS.indent)
