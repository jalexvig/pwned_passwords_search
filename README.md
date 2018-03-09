# Intro

Recently Troy Hunt set up a website that allows you to check if your password has been leaked.

> Pwned Passwords are half a billion real world passwords previously exposed in data breaches. This exposure makes them unsuitable for ongoing use as they're at much greater risk of being used to take over other accounts.

You can check if your password has been compromised on [his site](https://haveibeenpwned.com/Passwords), but if you are uncomfortable submitting your passwords you can use this simple script.

# Getting started

You will need Python(3) and the file of leaked passwords ordered by hash ([torrent](https://downloads.pwnedpasswords.com/passwords/pwned-passwords-ordered-2.0.txt.7z.torrent)).

Once you have downloaded the passwords and unzipped them into the `data` directory you are ready to begin.

# Usage

Run the `main.py` file on the commandline with the password in question:

`python3 main.py password`

Found 3303003 occurences of your password in the database.

`python3 main.py passwordJ8$`

Not found.

You can also provide the password SHA1 hash using the `--hashed` flag:

`python3 main.py 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 --hashed`

Found 3303003 occurences of your password in the database.
