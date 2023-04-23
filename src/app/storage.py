import os.path as osp
import getopt
import json
import sys

storage = f'{osp.dirname(__file__)}/storage.data'
meta = f'{osp.dirname(__file__)}/meta.json'


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


def list_stored():
    with open(storage, 'r', encoding='utf-8') as open_storage:
        contents = open_storage.read()
        print(contents)
        return contents


def create_storage_file():
    with open(storage, 'x', encoding='utf-8') as storage_open:
        i = input('\tDo you want to create one? [Y/n]: ')
        if i.lower() in ('y', 'yes'):
            storage_open.write()
        elif i.lower() in ('n', 'no'):
            print('\n\tYou can point to a storage file in a non-default location')  # noqa: E501
            choice = input('\n\t\tDo you want to specify a path? [Y/n]: ')

            if choice.lower() == 'y' or not choice:
                path = input('\n\tEnter the file path: ')
                print(path)


def write_dummy_data_to_storage():
    with open(storage, 'w', encoding='utf-8') as storage_open:
        i = input('\n\tDo you want to fill storage file with dummy data? [Y/n]: ')  # noqa: E501

        if i.lower() in ('y', 'yes') or not i:
            dummy_data = {
                1: 'first',
                2: [0, 1, 4, 8, 34, 42, 69, 420],
                3: '3',
                4: {'4.1': True, '4.2': None},
                5: ['one', 'two']
            }
            json.dump(dummy_data, storage_open, indent=4)
            print('\n=======================================================\n')  # noqa: E501
            print(f'\t\tStorage created:\n\t{storage}\n')
        elif i.lower() in ('n', 'no'):
            print('K thx bye')
            sys.exit(0)


def storage_check():
    print('\n\tChecking for a storage file . . .')
    print('++++++++++++++++++++++++++++++++++++++++++++++++++')  # noqa: E501
    try:
        with open(storage, 'r', encoding='utf-8') as storage_file:
            contents = storage_file.read()
            if contents != '' and contents is not None:
                print(f'\nStorage file located at:\n{storage}\n')
            else:
                print('\n\tStorage file exists but is empty')
                write_dummy_data_to_storage()
    except FileNotFoundError:
        print('\n\tNo storage file was found')
        create_storage_file()


def get_value_by_key(opt: str) -> str:  # sourcery skip: de-morgan
    with open(storage, 'r', encoding='utf-8') as storage_open:
        result = json.load(storage_open)
        if opt not in result.keys():
            print(f'\n\tNo key <<{opt}>> was found in storage\n')
            print('++++++++++++++++++++++++++++++++++++++++++++++++++\n')  # noqa: E501
            sys.exit(1)
        # if opt in result.keys():
        else:
            print(f'\nResult:\n\n{opt}: {result[opt]}\t\n')
            return result[opt]


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


def main():
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')  # noqa: E501
    print('KeyVaStoPy - a hastily designed key-value storage')
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
            elif sys.argv[2] == '--key' and sys.argv[4] == '--val':
                write_key_val_pair_to_storage()

    except getopt.GetoptError as err:
        print(err)
        sys.exit(err)


if __name__ == '__main__':
    main()
