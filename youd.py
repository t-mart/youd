import sys
import random
import base64
import uuid

B32_SPACE = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ234567')
B32_LEN = 26


def keep_only_b32(s):
    out = ""
    for c in s:
        if c in B32_SPACE:
            out += c
    return out


def readable_uuid(start_word):
    u = keep_only_b32(start_word[:24].upper())
    real_uuid = base64.b32encode(uuid.uuid4().bytes)[:B32_LEN]
    return u + real_uuid[-(B32_LEN - len(u)):]

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

    u = readable_uuid(start_word)

    sys.stdout.write(u)
    if sys.stdout.isatty():
        sys.stdout.write('\n')
    return 0
