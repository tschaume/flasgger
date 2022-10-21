# Fix for older setuptools
import re
import os

from setuptools import setup, find_packages


def fpath(name):
    return os.path.join(os.path.dirname(__file__), name)


def read(fname):
    return open(fpath(fname)).read()


def desc():
    return read('README.md')


# grep flasgger/__init__.py since python 3.x cannot
# import it before using 2to3
file_text = read(fpath('flasgger/__init__.py'))


def grep(attrname):
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)
    strval, = re.findall(pattern, file_text)
    return strval


setup(
    name='flasgger-tschaume',
    version=grep('__version__'),
    url='https://github.com/tschaume/flasgger/',
    license='MIT',
    author=grep('__author__'),
    author_email=grep('__email__'),
    description='Extract swagger specs from your flask project',
    long_description=desc(),
    long_description_content_type="text/markdown",
    packages=find_packages(
        exclude=[
            'tests', 'tests.*',
            'examples', 'examples.*',
            'demo_app', 'demo_app.*',
            'etc', 'etc.*'
        ]
    ),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>=0.10,<2.3',
        'PyYAML>=3.0',
        'jsonschema>=3.0.1',
        'mistune',
        'six>=1.10.0',
        'werkzeug',
    ],
    extras_require={
        'dev': [
            'marshmallow',
            'apispec>=1.0.0b5,<6',
            'apispec-webframeworks',
            'flask-restful',
            'pep8',
            'flake8',
            'pytest>=4.6',
            'flex',
            'coveralls',
            'pytest-cov',
            'decorator',
            'wheel',
            'flask-jwt',
            'readme_renderer',
            'setuptools>=40.4.2',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'flask.commands': [
            'generate-api-schema=flasgger.commands:generate_api_schema',
        ],
    },
)
