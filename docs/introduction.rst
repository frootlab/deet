Introduction
============

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

.. _SQLAlchemy: https://www.sqlalchemy.org
.. _Python: https://www.python.org/
.. _Frootlab: https://github.com/frootlab
.. _Project Infimum: https://github.com/orgs/frootlab/projects
