import os.path as osp
import getopt
import json
import sys

storage = f'{osp.dirname(__file__)}/storage.data'
meta = f'{osp.dirname(__file__)}/meta.json'

with open(meta, 'r', encoding='utf-8') as meta_open:
    contents = json.load(meta_open)
    if not contents or contents['version'] == '':
        print('\n\tNo database file seems to exist\n')
        i = input('\tDo you want to create one (with some test data)? [Y/n]: ')

        if i in 'Y' or not i:
            with open(storage, 'x', encoding='utf-8') as storage_open:
                dummy_data = {
                    1: 'first',
                    2: 2,
                    3: [0, 1, 4, 8, 13, 14, 34, 42, 69, 88],
                    4: None,
                    5: True,
                    6: '6'
                }
                json.dump(
                    dummy_data,
                    storage_open,
                    indent=4
                )
                print(
                    f'\n\t\tStorage file created in {osp.dirname(__file__)}'
                )
                print(storage_open)


def usage():
    usage_message = '\n\t\t   USAGE:\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'  # noqa: E501"
    usage_pt1 = 'storage -h/--help\t\tDisplay this help\n'
    usage_pt2 = 'storage    --key=[KEY]\t\tGet value of a key\n'
    usage_pt3 = 'storage    --key --val=[VAL]\tSet value of a key\n'  # noqa: E501
    # usage_pt4 = "\tstorage.py -d/--delete [KEY]\t\tDelete the key\n"
    print(usage_message, usage_pt1, usage_pt2, usage_pt3)
    return {}


def ver():
    with open(meta, 'r', encoding='utf-8') as R:
        contents = json.load(R)
        print(f"\t\tVersion: {contents.get('version')}")
        print('==================================================\n')  # noqa: E501
        # return {}

        # return R_contents["version"] if R_contents['version'] else 'Achtung! No version number was detected'  # noqa: E501
        # if R_contents["version"]:
        # print(f'\n\t\tVersion:\t\t\t{R_contents["version"]}')
        # - `[Error(101)]` means "`README_PATHmd` file exists,
        # but version is not defined within it"
        # - `[Error(102)]` means "`README.md` file doesn't exist at all,    # noqa: E501
        # or has an unexpected name (i.e. *NOT* `meta.json`),
        # or is in an unexpected location"
    # except FileNotFoundError:
        # return '\n\t[Error(102)]:\tCannot read app version (`meta.json` file does not exist,\n\t\thas an unexpected name or is placed in an unexpected location),\n\t\tplz contact the ret^W dev\n'  # noqa: E501
        # elif not R_contents["version"]:
        # return R_contents["version"]


def list_stored():
    with open(storage, 'r', encoding='utf-8') as open_storage:
        contents = open_storage.read()
        print(contents)
        return contents


def storage_check():
    with open(storage, 'r', encoding='utf-8') as open_storage:
        contents = open_storage.read()

        if contents == '':

            print('\n\tNo database file seems to exist\n')
            i = input('\tDo you want to create one (with some test data)? [Y/n]: ')  # noqa: E501

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
                    print(f'\t\tStorage created:\n\n{storage}\n')
            elif i.lower() == 'n':
                print('\n\tYou can point to a storage file in a non-default location')  # noqa: E501
                choice = input('\n\t\tDo you want to specify a path? [Y/n]: ')

                if choice.lower() == 'y' or not choice:
                    path = input('\n\tEnter the file path: ')
                    print(f'\n\t{path}\n\tTODO: - [ ] implement custom path functionality')  # noqa: E501
                    # pathlib.Path(path).parent.mkdir(parents=True)


def get_value_by_key(opt: str) -> str:  # sourcery skip: de-morgan
    with open(storage, 'r', encoding='utf-8') as storage_open:
        result = json.load(storage_open)
        if opt not in result.keys():
            print(f'\n\t\t\tNo key {opt} was found in the storage\n')
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')  # noqa: E501
            sys.exit(1)
        # if opt in result.keys():
        else:
            print(f'\nResult:\n\n{opt}: {result[opt]}\t\n')
            return result[opt]


"""
def write_key_val_pair_to_storage(key, val):
    with open(storage, 'r', encoding='utf-8') as storage_open:
        storage_loaded = json.load(storage_open)
        cached = dict(storage_loaded)

        if cached.get(sys.argv[2]) and cached.get(sys.argv[2]) is None:
            cached[sys.argv[2]].update(
                {cached[sys.argv[2]]: sys.argv[4]})
            print(cached[sys.argv[2]])
            return storage_loaded
        if cached[sys.argv[2]].isinstance(list):
            cached[sys.argv[2]].append(sys.argv[4])
            print({cached[sys.argv[2]]})
            with open(storage, 'w', encoding='utf-8') as storage_open:  # noqa: E501
                json.dump(cached, storage_open, indent=4)
                return storage_open
        if cached[sys.argv[2]].isinstance(dict) and len(sys.argv) < 5:
            cached[sys.argv[2]].update(sys.argv[4])
            cached[sys.argv[2]].update({sys.argv[4]: sys.argv[5]})  # noqa: E501
            with open(storage, 'w', encoding='utf-8') as storage_open:  # noqa: E501
                json.dump(cached, storage_open, indent=4)
                return storage_open
"""


def main():
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')  # noqa: E501
    print('KeyVaStoPy -- a hastily designed key-value storage')
    storage_check()

    try:
        opts, args = getopt.getopt(
            sys.argv[1:],
            'hvl',
            [
                'version'
                'help',
                'list',
                'key=',
                'val='
            ]
        )
        if not opts:
            ver()
            usage()
            sys.exit(0)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                usage()
            elif opt in ('-v', '--version'):
                ver()
            elif opt in ('-l', '--list'):
                list_stored()
            elif opt == '--key':
                get_value_by_key(arg)
            elif opt == '--val':
                return None
                # write_key_val_pair_to_storage(args)
            # elif str(opt) == '--key':
                # with open(storage, mode='r', encoding='utf-8') as open_storage:  # noqa: E501
                # storage_contents = json.load(open_storage)
                # if arg not in storage_contents.keys():
                # print('Key not found in storage')
                # else:
                # print(f'{opt}: {storage_contents.get(sys.argv[2])}')

    except getopt.GetoptError as err:
        print(err)
        sys.exit(err)


if __name__ == '__main__':
    main()
