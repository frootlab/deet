<div align="center">
  <img src="https://www.frootlab.org/images/fig/deet.svg" width=350px>
</div>

Deet
=======

[![Building Status](https://travis-ci.org/frootlab/deet.svg?branch=master)](https://travis-ci.org/frootlab/deet)
[![Documentation Status](https://readthedocs.org/projects/deet/badge/?version=latest)](https://deet.readthedocs.io/en/latest/?badge=latest)
[![PIP Version](https://badge.fury.io/py/deet.svg)](https://badge.fury.io/py/deet)

*Deet* is a universal data mapper and SQL-Database engine, that implements
high-performance and security requirements for large-scale enterprise analytical
applications.

The primary goal of Deet is to separate data integration and data analysis
into independent tasks, by providing a universal data interface for machine
learning- and data analysis applications. To achieve this goal, Deet
implements the two fundamental layers of a data warehouse:

The *integration layer* of Deet utilizes
[SQLAlchemy](https://www.sqlalchemy.org) to allow it\'s connection to a variety
of SQL-Databases (e.g. IBM DB2, Oracle, SAP, MS-SQL, MS-Access, Firebird,
Sybase, MySQL, Postgresql, SQLite, etc.). Thereupon it provides native support
for flat file databases (e.g. CSV-Tables, R-Table exports), laboratory
measurements and data generators.

The *staging layer* of Deet is implemented as a native SQL-Database engine,
featuring a DB-API 2.0 interface with full SQL:2016 support, a vertical data
storage manager and real-time encryption. This allows the data analysis
application to integrate a variety of different data sources, by using a unified
data interface (and SQL dialect).

Deet is open source, based on the
[Python](https://www.python.org/) programming language and actively developed as
part of the [Vivid Code](https://www.frootlab.org/vivid) framework
at [Frootlab](https://www.frootlab.org). Deet is developed as a generic
data interface, which can be integrated into data analysis applications, to
facilitate the integration of data.

Current Development Status
--------------------------

Deet currently is in *Pre-Alpha* development stage, which immediately follows
the *Planning* stage. This means, that at least some essential requirements of
Deet are not yet implemented. A comprehensive list of all currently supported
data back-ends is given in the [online
manual](https://deet.readthedocs.io/en/latest/).

Installation
------------

Comprehensive information and installation support is provided within the
[online manual](https://deet.readthedocs.io/en/latest/). If you already have
a Python environment configured on your computer, you can install the latest
distributed version by using pip:

    $ pip install deet

Documentation
-------------

The latest Deet documentation is available as an [online
manual](https://deet.readthedocs.io/en/latest/) and for download in the
formats [PDF](https://readthedocs.org/projects/deet/downloads/pdf/latest/),
[EPUB](https://readthedocs.org/projects/deet/downloads/epub/latest/) and
[HTML](https://readthedocs.org/projects/deet/downloads/htmlzip/latest/).

Contribute
----------

Contributors are very welcome! Feel free to report bugs and feature requests to
the [issue tracker](https://github.com/frootlab/deet/issues) provided by
GitHub. Currently, as the Frootlab Developers team still is growing, we do not
provide any Contribution Guide Lines to collaboration partners. However, if you
are interested to join the team, we would be glad, to receive an informal
[application](mailto:application@frootlab.org).

License
-------

Deet is [open source](https://github.com/frootlab/deet) and available free
for any use under the [GPLv3 license](https://www.gnu.org/licenses/gpl.html):

    © 2019 Frootlab Developers:
      Patrick Michl <patrick.michl@frootlab.org>
    © 2018-2019 Patrick Michl
