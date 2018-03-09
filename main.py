NUM_LINES = 501636842
BYTES_LINE = 63


def search(f, sha_pw, line_no=NUM_LINES // 2, last2=(0, 0)):

    # Password is past bounds
    if line_no < 0 or line_no >= NUM_LINES:
        return

    # Password is between others
    if line_no in last2:
        return

    f.seek(line_no * BYTES_LINE)

    sha, val = f.readline().rstrip().split(':')

    if sha == sha_pw:
        return val

    offset = abs(line_no - last2[-1]) // 2 or 1

    last = (last2[-1], line_no)

    if sha < sha_pw:
        return search(f, sha_pw, line_no=line_no + offset, last2=last)
    else:
        return search(f, sha_pw, line_no=line_no - offset, last2=last)


if __name__ == '__main__':

    import argparse
    import hashlib

    parser = argparse.ArgumentParser()
    parser.add_argument('hash', help='SHA-1 hash of password')
    parser.add_argument('--hashed', action='store_true')
    args = parser.parse_args()

    if not args.hashed:
        args.hash = hashlib.sha1(args.hash.encode()).hexdigest()

    with open('data/pwned-passwords-ordered-2.0.txt') as f:
        res = search(f, args.hash.upper())

        if res is None:
            print('Not found.')
        else:
            print('Found %s occurences of your password in the database.' % res)
