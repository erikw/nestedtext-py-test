import sys
from pprint import pprint

import nestedtext as nt


def test_from_file():
    addressbook = {}
    try:
        addressbook = nt.load("conf/addressbook.nt", top="dict")
    except nt.NestedTextError as e:
        e.terminate()
    except OSError as e:
        print(e, file=sys.stderr)
        sys.exit(1)
    pprint(addressbook)
    pprint(addressbook["president"]["name"])
    pprint(type(addressbook["president"]["name"]))


def main():
    test_from_file()


if __name__ == "__main__":
    sys.exit(main())
