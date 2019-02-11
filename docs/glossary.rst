Glossary
========

Database Engine Glossary
~~~~~~~~~~~~~~~~~~~~~~~~

.. glossary::

    Row Like

        *Row like* data comprises different data formats, which are used to
        represent table records. This includes tuples, mappings and instances of
        the :class:`Record class <nemoa.db.table.Record>`. The :class:`Table
        class <nemoa.db.table.Table>` accepts these data types for appending
        rows by :meth:`~nemoa.db.table.Table.insert` and for retrieving rows by
        :meth:`~nemoa.db.table.Table.select`.

    Cursor Mode

        The *cursor mode* defines the *scrolling type* and the *operation mode*
        of a cursor. Internally the respective parameters of the
        :class:`Cursor class <nemoa.db.table.Cursor>` are identified by binary
        flags. The public interface uses a string representation, given by
        the space separated names of the scrolling type and the the operation
        mode. Supported scrolling types are:

        :forward-only: The default scrolling type of cursors is called a
            forward-only cursor and can move only forward through the result
            set. A forward-only cursor does not support scrolling but only
            fetching rows from the start to the end of the result set.
        :scrollable: A scrollable cursor is commonly used in screen-based
            interactive applications, like spreadsheets, in which users are
            allowed to scroll back and forth through the result set. However,
            applications should use scrollable cursors only when forward-only
            cursors will not do the job, as scrollable cursors are generally
            more expensive, than forward-only cursors.
        :random: Random cursors move randomly through the result set. In
            difference to a randomly sorted cursor, the rows are not unique and
            the number of fetched rows is not limited to the size of the result
            set. If the method :meth:`.fetch` is called with a zero value for
            size, a CursorModeError is raised.

        Supported operation modes are:

        :dynamic: A **dynamic cursor** is built on-the-fly and therefore
            comprises any changes made to the rows in the result set during it's
            traversal, including new appended rows and the order of it's
            traversal. This behavior is regardless of whether the changes occur
            from inside the cursor or by other users from outside the cursor.
            Dynamic cursors are thread-safe but do not support counting filtered
            rows or sorting rows.
        :indexed: Indexed cursors (aka Keyset-driven cursors) are built
            on-the-fly with respect to an initial copy of the table index and
            therefore comprise changes made to the rows in the result set during
            it's traversal, but not new appended rows nor changes within their
            order. Keyset driven cursors are thread-safe but do not support
            sorting rows or counting filtered rows.
        :static: Static cursors are buffered and built during it's creation time
            and therefore always display the result set as it was when the cursor
            was first opened. Static cursors are not thread-safe but support
            counting the rows with respect to a given filter and sorting the
            rows.

    Aggregation Function

        *Aggregation Functions* are :class:`callable` objects, that transform
        sequences of objects of a given domain into a single value. Examples
        include :func:`len`, :func:`sum`, :func:`min` or :func:`max`, but
        depending on the domain, many out-of-the-box aggregators are shipped
        with the standard library package :mod:`statistics` or with third party
        packages like :mod:`numpy`.
