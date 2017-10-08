import os

from setuptools import find_packages, setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='malickosti-v-akvarelkach',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description="Website application for Maličkosti v akvarelkách",
    long_description=README,
    url='https://github.com/just-paja/malickosti-v-akvarelkach',
    author='Pavel Žák',
    author_email='pavel@zak.global',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
