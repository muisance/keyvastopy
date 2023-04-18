import pathlib
import getopt
import json
import sys

STORAGE_PATH = pathlib.Path('storage.data')
print(STORAGE_PATH)

METADATA_PATH = pathlib.Path('meta.json')
print(METADATA_PATH)

if not STORAGE_PATH.exists() or STORAGE_PATH.read() == '' or STORAGE_PATH.get('version') == '':
    print('\n\tNo database file seems to exist\n')
    i = input('\tDo you want to create one (with some test data)? [Y/n]: ')

    if i in 'Y' or not i:
        with open(STORAGE_PATH, 'x', encoding='utf-8') as OPEN_STORAGE:
            test_data = {
                1: 'first',
                2: 2,
                3: [0, 1, 4, 8, 13, 14, 34, 42, 69, 88],
                4: None,
                5: True,
                6: '6'
            }
            json.dump(
                test_data,
                OPEN_STORAGE,
                indent=4
            )
            print(
                f'\n\t\tStorage file created in this directory ({pathlib.Path(__file__)})')
            print(OPEN_STORAGE)


def versioning() -> str:
    try:
        with open(METADATA_PATH, 'r', encoding='utf-8') as R:
            R_contents = json.load(R)

            if R_contents["version"]:
                print(f'\n\t\tVersion:\t\t\t{R_contents["version"]}')
                # * - `[Error(101)]` means "`README_PATHmd` file exists,
                # * but version is not defined within it"
                # * - `[Error(102)]` means "`README.md` file doesn't exist at all,
                # * or has an unexpected name (i.e. *NOT* `meta.json`),
                # * or is in an unexpected location"

            if R_contents["version"] == '' or not R_contents["version"]:
                return f'\n\t[Error(101)]:\tCannot read app version (`version` field can not be located in a file),\n\t\tplz contact the ret^W dev\n'
    except FileNotFoundError:
        return f'\n\t[Error(102)]:\tCannot read app version (`meta.json` file does not exist,\n\t\thas an unexpected name or is placed in an unexpected location),\n\t\tplz contact the ret^W dev\n'


def usage() -> str:
    usage_message: str = "\nUSAGE:\n"
    usage_pt1: str = "\tstorage.py -h/--help\t\t\tCall this help and exit\n"
    usage_pt2: str = "\tstorage.py -k/--key [KEY]\t\tGet the value of the key\n"
    usage_pt3: str = "\tstorage.py -s/--set [KEY] [VALUE]\tSet the value of the key\n"
    usage_pt4: str = "\tstorage.py -d/--delete [KEY]\t\tDelete the key\n"
    print(usage_message, usage_pt1, usage_pt2, usage_pt3, usage_pt4)
    return {}


def handle_usage(*args: str | list[str]) -> None:
    try:
        opts = getopt.getopt(
            sys.argv[:1],
            'hcVvvlk:v:s:',
            [
                'help',
                'create',
                'verbose',
                'version',
                'list',
                'key=',
                'val='
            ],
        )
    except getopt.GetoptError as err:
        usage()
        print(err)
        sys.exit(err)

    for o in opts:
        if o in ('-h', '--help') or args[0] == '--help':
            usage()
            sys.exit(0)

    if len(*args[:1]) < 1:
        usage()
        sys.exit(0)

    if args[0] in ('V', '--version'):
        print(versioning())


def read_storage(store: __path__) -> dict:
    return json.load(store)


def write_storage(store: __path__) -> dict:
    return STORAGE_PATH.write(store)


def update_storage(store: __path__):
    return STORAGE_PATH.update(store)


def main() -> dict:
    if not STORAGE_PATH.exists():
        with open(STORAGE_PATH, 'x', encoding='utf-8') as open_storage:
            json.dump(open_storage,)
    else:
        with open(STORAGE_PATH, 'r') as read_storage:
            STORAGE_PATH.update(read_storage)

    return STORAGE_PATH


if __name__ == '__main__':
    main()
