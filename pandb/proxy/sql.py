# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
#
# This file is part of Pandora, https://www.frootlab.org/pandora
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
"""Table Proxy Classes."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from pandb.core import table

#
# Classes
#

class Table(table.Proxy):
    """SQL-Table Proxy."""
