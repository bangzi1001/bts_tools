#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# bitshares_delegate_tools - Tools to easily manage the bitshares client
# Copyright (c) 2014 Nicolas Wack <wackou@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup, find_packages
import os.path

here = os.path.abspath(os.path.dirname(__file__))
#README = open(os.path.join(here, 'README.rst')).read()
#HISTORY = open(os.path.join(here, 'HISTORY.rst')).read()
HISTORY = """Unreleased as of yet"""

VERSION = '0.1.dev1'


install_requires = ['Flask', 'requests'] #, 'SQLAlchemy', 'Flask-SQLAlchemy']

setup_requires = []

entry_points = {
    'console_scripts': [
        'bts = bitshares_delegate_tools.cmdline:main'
    ],
}


args = dict(name='bitshares_delegate_tools',
            version=VERSION,
            description='BitShares delegate tools',
            long_description='BitShares delegate tools',
            # Get strings from
            # http://pypi.python.org/pypi?%3Aaction=list_classifiers
            classifiers=['Development Status :: 2 - Pre-Alpha',
                         'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                         'Operating System :: OS Independent',
                         'Programming Language :: Python :: 2',
                         'Programming Language :: Python :: 2.7',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.4',
                         ],
            keywords='BitShares delegate tools',
            author='Nicolas Wack',
            author_email='wackou@gmail.com',
            url='https://github.com/wackou/bitshares_delegate_tools',
            packages=find_packages(),
            include_package_data=True,
            #package_data = { 'bitshares_delegate_tools': ['bitshares_delegate_tools/static/css/*'] },
            install_requires=install_requires,
            setup_requires=setup_requires,
            entry_points=entry_points,
            )

setup(**args)