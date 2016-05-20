****
youd
****

Generate a random base32-encoded uuid (A-Z,2-7) with an optional readable word in the beginning.

===========
Description
===========

By default, youd generate a random base32-encoded uuid.

If you provide a string as the first argument to this script, it will replace the first characters of this otherwise random uuid.

Only characters of the word that are in the (A-Z, 2-7) space will be placed. Lower cased letters that are provided are
converted to upper case.

Why? Sometimes, you're writing tests or documentation and you need a uuid, but also want it to be readable and meaningful. What's
going to convey more to users? RPRKIRYJSVMWSOY64XS3CIL3OO or SPECIALUUID6JIHP5RKUQBPDQI ?

============
Installation
============

.. code-block:: bash

    $ git clone https://github.com/t-mart/youd.git
    $ cd youd
    $ pip install --editable .

=====
Usage
=====

.. code-block:: bash

    $ youd
    NFZLD7S6ONFJVLPGULVJKJG2FU

    $ youd "Special Uuid lol" # create a "readable" uuid
    SPECIALUUIDLOLO3CU2NOVNCXI

    $ youd | pbcopy # place uuid in clipboard

