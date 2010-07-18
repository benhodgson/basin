from distutils.core import setup

setup(
    name='basin',
    version='0.1',
    description='A Python module for generating string representations of '
        'integers and bytestrings with arbitrary base and alphabet.',
    py_modules=['basin'],
    url='http://github.com/benhodgson/basin',
    author='Ben Hodgson',
    author_email='ben@benhodgson.com',
    keywords = ['base', 'base32', 'base62', 'base64'],
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
