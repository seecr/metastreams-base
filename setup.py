## begin license ##
#
# "Metastreams-Base" is the base package for all Metastreams modules.
#
# Copyright (C) 2021 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Metastreams-Base"
#
# "Metastreams-Base" is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# "Metastreams-Base" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Metastreams-Base"; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
## end license ##

from distutils.core import setup

setup(
    name='metastreams-base',
    packages=[
        'metastreams',
        'metastreams.base',
    ],
    version='%VERSION%',
    url='https://metastreams.nl',
    author='Seecr',
    author_email='info@seecr.nl',
    description='Metastreams-Base is the base package for all Metastreams modules.',
    long_description='Metastreams-Base is the base package for all Metastreams modules.',
    license='GNU Public License',
    platforms='all',
)
