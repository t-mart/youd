import sys
import random

B32_SPACE = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
B32_LEN = 26


def keep_only_b32(s):
    out = ""
    for c in s:
        if c in B32_SPACE:
            out += c
    return out


def readable_uuid(start_word):
    uuid = keep_only_b32(start_word[:B32_LEN].upper())

    if len(uuid) < B32_LEN:
        diff = B32_LEN - len(uuid)
        uuid += ''.join(random.choice(B32_SPACE) for _ in xrange(diff))

    return uuid

"""
Generate a random base32-encoded uuid (A-Z,2-7) with an optional readable word in the beginning.

If you provide a string as the first argument to this script, it will replace the first characters of this otherwise random uuid.

Only characters of the word that are in the (A-Z, 2-7) space will be placed. Lower cased letters that are provided are
converted to upper case.

Why? Sometimes, you're writing tests or documentation and you need a uuid, but also want it to be readable and meaningful. What's
going to convey more to users? RPRKIRYJSVMWSOY64XS3CIL3OO or SPECIALUUID6JIHP5RKUQBPDQI ?

The second uuid there was created by running the script like this:
  $ youd "special uuid"
"""
def main():
    start_word = ""
    if len(sys.argv) > 1:
        start_word = sys.argv[1]

    uuid = readable_uuid(start_word)

    sys.stdout.write(uuid)
    if sys.stdout.isatty():
        sys.stdout.write('\n')
    return 0
