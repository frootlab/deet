<div align="center">
  <a href="https://github.com/frootlab/pandora">
    <img src="https://bit.ly/2O2V8Je">
  </a><br>
</div>

Pandora
=======

[![Building Status](https://travis-ci.org/frootlab/pandb.svg?branch=master)](https://travis-ci.org/frootlab/pandb)
[![Documentation Status](https://readthedocs.org/projects/pandora/badge/?version=latest)](https://pandora.readthedocs.io/en/latest/?badge=latest)
[![PIP Version](https://badge.fury.io/py/pandb.svg)](https://badge.fury.io/py/pandb)

*Pandora* is a universal database proxy and SQL-Database engine, that implements
high-performance and security requirements for large-scale enterprise analytical
applications.

The primary goal of Pandora is to separate data integration and data analysis
into independent tasks, by providing a unified (universal) data interface for
machine learning- and data analysis applications. To achieve this goal, Pandora
implements the two fundamental layers of a data warehouse:

The *integration layer* of Pandora utilizes
[SQLAlchemy](https://www.sqlalchemy.org) to allow it\'s connection to a variety
of SQL-Databases (e.g. IBM DB2, Oracle, SAP, MS-SQL, MS-Access, Firebird,
Sybase, MySQL, Postgresql, SQLite, etc.). Thereupon it provides native support
for flat file databases (e.g. CSV-Tables, R-Table exports), laboratory
measurements and data generators.

The *staging layer* of Pandora is implemented as a native SQL-Database engine,
featuring a DB-API 2.0 interface with full SQL:2016 support, a vertical data
storage manager and real-time encryption. This allows the data analysis
application to integrate a variety of different data sources, by using a unified
data interface (and SQL dialect).

Pandora is [open source](https://github.com/frootlab/pandora), based on the
[Python](https://www.python.org/) programming language and actively developed as
part of the [Smart Analytics](https://github.com/orgs/frootlab/projects) project
at [Frootlab](https://github.com/frootlab). Pandora is developed as a generic
data interface, which can be integrated into data analysis applications, to
facilitate the integration of data.

Current Development Status
--------------------------

Pandora currently is in *Pre-Alpha* development stage, which immediately follows
the *Planning* stage. This means, that at least some essential requirements of
Pandora are not yet implemented. A comprehensive list of all currently supported
data back-ends is given in the [online
manual](https://pandora.readthedocs.io/en/latest/).

Installation
------------

Comprehensive information and installation support is provided within the
[online manual](https://pandora.readthedocs.io/en/latest/). If you already have
a Python environment configured on your computer, you can install the latest
distributed version by using pip:

    $ pip install pandb

Documentation
-------------

The latest Pandora documentation is available as an [online
manual](https://pandora.readthedocs.io/en/latest/) and for download in the
formats [PDF](https://readthedocs.org/projects/pandora/downloads/pdf/latest/),
[EPUB](https://readthedocs.org/projects/pandora/downloads/epub/latest/) and
[HTML](https://readthedocs.org/projects/pandora/downloads/htmlzip/latest/).

Contribute
----------

Contributors are very welcome! Feel free to report bugs and feature requests to
the [issue tracker](https://github.com/frootlab/pandora/issues) provided by
GitHub. Currently, as the Frootlab Developers team still is growing, we do not
provide any Contribution Guide Lines to collaboration partners. However, if you
are interested to join the team, we would be glad, to receive an informal
[application](mailto:application@frootlab.org).

License
-------

Pandora is [open source](https://github.com/frootlab/pandora) and available free
for any use under the [GPLv3 license](https://www.gnu.org/licenses/gpl.html):

    © 2019 Frootlab Developers:
      Patrick Michl <patrick.michl@frootlab.org>
    © 2018-2019 Patrick Michl
