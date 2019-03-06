Pandora
=======

.. image:: https://travis-ci.org/frootlab/pandb.svg?branch=master
   :target: https://travis-ci.org/frootlab/pandb

.. image:: https://readthedocs.org/projects/pandora/badge/?version=latest
    :target: https://pandora.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/pandb.svg
    :target: https://badge.fury.io/py/pandb

*Pandora* is a universal database proxy and SQL-Database engine, that implements
high-performance and security requirements for enterprise analytical
applications.

The primary goal of Pandora is to provide a unified (universal) data interface
for machine learning- and data analysis applications, to facilitate their
integration into existing operational data landscapes. To achieve this goal,
Pandora implements the two fundamental layers of a data warehouse:

The *integration layer* of Pandora utilizes `SQLAlchemy`_ to allow it's
connection to a variety of SQL-Databases (e.g. IBM DB2, Oracle, SAP, MS-SQL,
MS-Access, Firebird, Sybase, MySQL, Postgresql, SQLite, etc.). Thereupon it
provides native support for flat file databases (e.g. CSV-Tables, R-Table
exports), laboratory measurements and data generators.

The *staging layer* of Pandora is implemented as a native SQL-Database engine,
featuring a DB-API 2.0 interface with full SQL:2016 support, a vertical data
storage manager and real-time encryption. This allows the data analysis
application to integrate a variety of different data sources, by using a unified
data interface (and SQL dialect).

Pandora is open source, based on the `Python`_ programming language and actively
developed as part of `Project Infimum`_ at `Frootlab`_.

Development Status
------------------

Pandora currently is in *Pre-Alpha* state, which immediately follows the
project's *planning* phase. This means, that at least some essential
requirements of Pandora are not yet implemented.

Install
-------

Pandora is hosted on `PyPI`_, which allows to install the latest packaged
version of Pandora by using pip::

    $ pip install pandb

Further information and support is provided within the `installation manual`_.

Documentation
-------------

The latest Pandora documentation is available `online`_ and offline in the
formats `PDF`_, `Epub`_ and zipped `HTML`_.

Contribute
----------

Contributors are very welcome! Feel free to report bugs and feature requests to
the `issue tracker`_ provided by GitHub.

License
-------

Pandora is available free for any use under the `GPLv3 license`_::

   Copyright (C) 2019 Frootlab Developers
   Patrick Michl <patrick.michl@gmail.com>

The source code is available at `GitHub`_.

.. _Python: https://www.python.org/
.. _SQLAlchemy: https://www.sqlalchemy.org
.. _PyPI: https://pypi.org/project/pandb/
.. _Installation Manual: https://pandora.readthedocs.io/en/latest/install.html
.. _online documentation: https://pandora.readthedocs.io/en/latest/
.. _PDF: https://readthedocs.org/projects/pandora/downloads/pdf/latest/
.. _Epub: https://readthedocs.org/projects/pandora/downloads/epub/latest/
.. _HTML: https://readthedocs.org/projects/pandora/downloads/htmlzip/latest/
.. _issue tracker: https://github.com/frootlab/pandora/issues
.. _GPLv3 license: https://www.gnu.org/licenses/gpl.html
.. _Frootlab: https://github.com/frootlab
.. _Project Infimum: https://github.com/orgs/frootlab/projects
