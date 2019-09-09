# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
#
# This file is part of Pandora, https://github.com/frootlab/motley
#
#  Pandora is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Pandora is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Pandora. If not, see <http://www.gnu.org/licenses/>.
#
"""Unittests for module 'pandb.core.table'."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from typing import Any
from hup.base import test
from pandb.core import table

#
# Test Cases
#

class TestTable(test.ModuleTest):
    module = table

    def test_Table(self) -> None:
        pass

    def test_Table_create(self) -> None:
        kwds: dict

        kwds = {'columns': ('a', )}
        with self.subTest(**kwds):
            tbl = table.Table()
            tbl.create(None, **kwds)
            self.assertEqual(tbl.fields[0].name, 'a')
            self.assertEqual(tbl.fields[0].type, 'typing.Any')
            self.assertEqual(len(tbl.fields[0].metadata), 0)

        kwds = {'columns': (('a', str), )}
        with self.subTest(**kwds):
            tbl = table.Table()
            tbl.create(None, **kwds)
            self.assertEqual(tbl.fields[0].name, 'a')
            self.assertEqual(tbl.fields[0].type, str)
        kwds = {'columns': (('b', int, {'default': ''}), )}

        with self.subTest(**kwds):
            tbl = table.Table()
            tbl.create(None, **kwds)
            self.assertEqual(tbl.fields[0].name, 'b')
            self.assertEqual(tbl.fields[0].type, int)
            self.assertEqual(tbl.fields[0].default, '')

        kwds = {'columns': (('_a', Any, {'metadata': {1: 1, 2: 2}}), )}
        with self.subTest(**kwds):
            tbl = table.Table()
            tbl.create(None, **kwds)
            self.assertEqual(tbl.fields[0].name, '_a')
            self.assertEqual(tbl.fields[0].type, Any)
            self.assertEqual(len(tbl.fields[0].metadata), 2)
