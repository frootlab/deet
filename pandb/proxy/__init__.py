# -*- coding: utf-8 -*-
# Copyright (c) 2019 Patrick Michl
#
# This file is part of pandora, https://frootlab.github.io/pandora
#
#  pandora is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  pandora is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  pandora. If not, see <http://www.gnu.org/licenses/>.
#
"""Database and Data Warehouse."""

__author__ = 'Patrick Michl'
__email__ = 'frootlab@gmail.com'
__license__ = 'GPLv3'
__docformat__ = 'google'

from flab.base import pkg
from pandb.core import table
from flab.errors import ConnectError
from flab.base.types import Any, Module

#
# Constructors
#

def connect(name: str, *args: Any, **kwds: Any) -> table.Proxy:
    """Connect Table Proxy

    Args:
        name: Name of module, which is used to connect a Table Proxy.
        *args: Arguments, that are passed to the class 'Table' of the given
            module.
        **kwds: Keyword arguments, that are passed to the class 'Table' of the
            given module.

    """
    module = pkg.get_submodule(name=name)
    if not isinstance(module, Module):
        raise ConnectError(f"module '{name}' does not exist")
    if not hasattr(module, 'Table'):
        raise ConnectError(f"module '{name}' does not contain a 'Table' class")
    return module.Table(*args, **kwds) # type: ignore
