Data Integration
================

The *integration layer* of Deet utilizes `SQLAlchemy`_ to allow it's
connection to a variety of SQL-Databases (e.g. IBM DB2, Oracle, SAP, MS-SQL,
MS-Access, Firebird, Sybase, MySQL, Postgresql, SQLite, etc.). Thereupon it
provides native support for flat file databases (e.g. CSV-Tables, R-Table
exports), laboratory measurements and data generators. The following table gives
an overview of the currently supported back-ends:

+---------------+----------+-----------+----------+----------+----------+
|               | Planning | Pre-Alpha | Alpha    | Beta     | Stable   |
+===============+==========+===========+==========+==========+==========+
| IBM-DB2       |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| Oracle        |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| SAP           |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| MySQL         |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| Postgresql    |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| SQLite        |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| CSV-Tables    |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
| R CSV-Exports |          |           |          |          |          |
+---------------+----------+-----------+----------+----------+----------+
