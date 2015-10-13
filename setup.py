from setuptools import setup

setup(
    name = 'veryfay',
    version = '0.1.0',
    tests_require=["behave>=1.2.4", "pyhamcrest>=1.8.5"],
	packages=['veryfay'],
	description = 'A library for activity based authorization.',
    author = 'Florin Nitoi',
    author_email = 'florin.nitoi@gmail.com',
    license = 'MIT',
    keywords = 'authorization engine library activity role permission',
    )