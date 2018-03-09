import os
from glob import glob
import re


def _init_dict():

    num_range = list(range(ord('0'), ord('9') + 1))
    char_range = list(range(ord('A'), ord('Z') + 1))

    d = {chr(x): [] for x in num_range + char_range}

    return d


def _write_dict(d, dpath_data='data'):

    for c, vals in d.items():
        fpath_char = os.path.join(dpath_data, '%s.txt' % c)
        with open(fpath_char, 'a') as f:
            f.write('\n'.join(vals))


def split_into_pieces(dpath_data='data', write_freq=100000):

    fpath_passwords = os.path.join(dpath_data, 'passwords.txt')

    d = _init_dict()

    with open(fpath_passwords) as f:
        for i, line in enumerate(f):
            s = line.rstrip()
            d[s[0]].append(s)

            if i > 0 and i % write_freq == 0:
                print('Writing at entry %i' % i)
                _write_dict(d, dpath_data)
                d = _init_dict()

    if d:
        _write_dict(d, dpath_data)


def combine_files(dpath='data'):

    fpaths = sorted([x for x in glob('data/*.txt') if re.match('data.[0-9A-Z]\.txt', x)])

    fpath_result = os.path.join(dpath, 'passwords_sorted.txt')

    for fpath_char in fpaths:

        print('Processing %s' % fpath_char.split(os.path.sep)[-1])

        with open(fpath_char) as f, open(fpath_result, 'a') as g:
            l = f.readlines()
            l.sort()
            g.write('\n'.join(l))


def check_num_lines_split_files(dpath='data'):

    fpaths = sorted([x for x in glob('%s/*.txt' % dpath) if re.match('%s.[0-9A-Z]\.txt' % dpath, x)])

    total = 0

    for fpath_char in fpaths:

        print('Processing %s' % fpath_char.split(os.path.sep)[-1])

        with open(fpath_char) as f:
            total += sum(1 for _ in f)

    print(total)


def check_no_dupes(dpath='data'):

    fpaths = sorted([x for x in glob('%s/*.txt' % dpath) if re.match('%s.[0-9A-Z]\.txt' % dpath, x)])

    for fpath_char in fpaths:
        print('Processing %s' % fpath_char.split(os.path.sep)[-1])
        with open(fpath_char) as f:
            num_uniqe = len(set(f))
            f.seek(0)
            num_total = len(f.readlines())
            if num_total != num_uniqe:
                print(num_uniqe, num_total)


if __name__ == '__main__':

    split_into_pieces()
    combine_files()

    # check_num_lines_split_files()
    # check_no_dupes()
