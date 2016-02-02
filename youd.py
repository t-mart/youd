import base64
import uuid
import sys


def gen():
    return base64.b32encode(uuid.uuid4().bytes)[:26].decode('utf-8')

def main():
    sys.stdout.write(gen())
    if sys.stdout.isatty():
        sys.stdout.write('\n')
    return 0
