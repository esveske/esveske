import pandas as pd
import os
import sys

data: pd.DataFrame = pd.read_excel('./data.xlsx')


_sanity_checks = []


def sanity_check(fn):
    _sanity_checks.append(fn)
    return fn


def error(*args):
    print(*args, file=sys.stderr)


@sanity_check
def no_404_links():

    ok = True
    for link in data['link']:
        if not os.path.exists('./gen/' + link):
            error('file', link, 'does not exist!')
            ok = False
    return ok


@sanity_check
def no_unlinked_pdfs():
    ok = True

    svi_linkovi = set(data['link'])

    for (dirpath, _, files) in os.walk('./gen/pdf/'):
        for file in files:
            if not file.endswith('.pdf'):
                continue
            non_prefixed = dirpath[6:] + '/' + file  # strip the './gen/' part
            if non_prefixed not in svi_linkovi:
                error('file', non_prefixed, 'not linked anywhere')
                ok = False
    return ok


if __name__ == "__main__":
    for check in _sanity_checks:
        if not check():
            print('check', check.__name__, 'failed, exiting')
            sys.exit(1)
