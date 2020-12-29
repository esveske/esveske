import pandas as pd
import os
import sys

data: pd.DataFrame = pd.read_excel('./data.xlsx', engine="openpyxl")


_sanity_checks = []

current_error = False

def sanity_check(fn):
    def _w():
        global current_error
        current_error = False
        fn()
        return not current_error
    _w.__name__ = fn.__name__
    _sanity_checks.append(_w)
    return _w


def error(*args):
    global current_error
    print(*args, file=sys.stderr)
    current_error = True


@sanity_check
def no_404_links():

    for link in data['link']:
        if not os.path.exists('./gen/' + link):
            error('file', link, 'does not exist!')


@sanity_check
def no_unlinked_pdfs():

    svi_linkovi = set(data['link'])

    for (dirpath, _, files) in os.walk('./gen/pdf/'):
        for file in files:
            if not file.endswith('.pdf'):
                continue
            non_prefixed = dirpath[6:] + '/' + file  # strip the './gen/' part
            if non_prefixed not in svi_linkovi:
                error('file', non_prefixed, 'not linked anywhere')


if __name__ == "__main__":
    for check in _sanity_checks:
        if not check():
            print('check', check.__name__, 'failed, exiting')
            sys.exit(1)
