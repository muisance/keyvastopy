import os.path as osp
import pathlib
import getopt
import json
import sys

storage = osp.abspath(__file__).replace('/storage.py', '/storage.data')
meta = osp.abspath(__file__).replace('/storage.py', '/meta.json')


def usage():
    usage_message = "\nUSAGE:\n"
    usage_pt1 = "\tstorage.py -h/--help\t\t\tCall this help and exit\n"
    usage_pt2 = "\tstorage.py -k/--key [KEY]\t\tGet the value of the key\n"
    usage_pt3 = "\tstorage.py -s/--set [KEY] [VALUE]\tSet the value of the key\n"  # noqa: E501
    usage_pt4 = "\tstorage.py -d/--delete [KEY]\t\tDelete the key\n"
    print(usage_message, usage_pt1, usage_pt2, usage_pt3, usage_pt4)
    return {}


def versioning() -> str:
    try:
        with open(meta, 'r', encoding='utf-8') as R:
            R_contents = json.load(R)

            if R_contents["version"]:
                print(f'\n\t\tVersion:\t\t\t{R_contents["version"]}')
                # - `[Error(101)]` means "`README_PATHmd` file exists,
                # but version is not defined within it"
                # - `[Error(102)]` means "`README.md` file doesn't exist at all,    # noqa: E501
                # or has an unexpected name (i.e. *NOT* `meta.json`),
                # or is in an unexpected location"

            if R_contents["version"] == '' or not R_contents["version"]:
                return '\n\t[Error(101)]:\tCannot read app version (`version` field can not be located in a file),\n\t\tplz contact the ret^W dev\n'  # noqa: E501
    except FileNotFoundError:
        return '\n\t[Error(102)]:\tCannot read app version (`meta.json` file does not exist,\n\t\thas an unexpected name or is placed in an unexpected location),\n\t\tplz contact the ret^W dev\n'  # noqa: E501


"""
if not storage.exists() or storage.read() == '' or storage.get('version') == '':  # noqa: E501
    print('\n\tNo database file seems to exist\n')
    i = input('\tDo you want to create one (with some test data)? [Y/n]: ')

    if i in 'Y' or not i:
        with open(storage, 'x', encoding='utf-8') as OPEN_STORAGE:
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
                f'\n\t\tStorage file created in this directory ({osp.curdir(__file__)})')
            print(OPEN_STORAGE)



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
    return storage.write(store)


def update_storage(store: __path__):
    return storage.update(store)


def main() -> dict:
    if not storage.exists():
        with open(storage, 'x', encoding='utf-8') as open_storage:
            json.dump(open_storage,)
    else:
        with open(storage, 'r') as read_storage:
            storage.update(read_storage)

    return storage
"""

with open(storage, 'r', encoding='utf-8') as open_storage:
    contents = open_storage.read()

    if contents == '':

        print('\n\tNo database file seems to exist\n')
        i = input('\tDo you want to create one (with some test data)? [Y/n]: ')

        if not i or i.lower() == 'y':
            dummy_data = {
                1: 'first',
                2: [0, 1, 4, 8, 34, 42, 69, 420],
                3: '3',
                4: {'4.1': True, '4.2': None},
                5: ['one', 'two']
            }
            with open(storage, 'w', encoding='utf-8') as open_storage:
                json.dump(dummy_data, open_storage, indent=4)
                print('\n=======================================================\n')  # noqa: E501
                print(f'\t\tDatabase created:\n\n{storage}\n')
        elif i.lower() == 'n':
            print('\n\tYou can point to a storage file in a non-default location')
            choice = input('\n\t\tDo you want to specify a path? [Y/n]: ')

            if choice.lower() == 'y' or not choice:
                path = input('\n\tEnter the file path: ')
                storage = path
    print('G\'bye!')
    sys.exit(0)


def main():
    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
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
    usage()
    for opt in opts:
        if opt in ('-h', '--help') or args[0] == '--help':
            usage()
            sys.exit(0)

        if opt in ('-V', '--version'):
            versioning()


if __name__ == '__main__':
    main()
