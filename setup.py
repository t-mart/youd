from setuptools import setup

setup(
        name='youd',
        url='https://github.com/t-mart/youd',
        description="generate a base32 random uuid.",
        author="Tim Martin",
        author_email='tim@timmart.in',
        entry_points={
            'console_scripts': [
                'youd = youd:main'
            ]
        },
)