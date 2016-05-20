from setuptools import setup

setup(
    name='youd',
    version='1.1.0',
    url='https://github.com/t-mart/youd',
    description="Generate a random base32-encoded uuid (A-Z,2-7) with an optional readable word in the beginning.",
    author="Tim Martin",
    author_email='tim@timmart.in',
    entry_points={
        'console_scripts': [
            'youd = youd:main'
        ]
    },
)