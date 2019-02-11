Install
=======

Pandora requires Python 3.7 or later. If you do not already have a Python
environment configured on your computer, please see the instructions for
installing the full `scientific Python stack <https://scipy.org/install.html>`_.

.. note::
   If you are using the Windows platform and want to install optional packages
   (e.g., `scipy`), then it may be useful to install a Python distribution such
   as:
   `Anaconda <https://www.anaconda.com/download/>`_,
   `Enthought Canopy <https://www.enthought.com/product/canopy>`_,
   `Python(x,y) <http://python-xy.github.io/>`_,
   `WinPython <https://winpython.github.io/>`_, or
   `Pyzo <http://www.pyzo.org/>`_.
   If you already use one of these Python distributions, please refer to their
   online documentation.

Below it is assumed, that you have the default Python environment configured on
your computer and you intend to install Pandora inside of it.  If you want
to create and work with Python virtual environments, please follow instructions
on `venv <https://docs.python.org/3/library/venv.html>`_ and `virtual
environments <http://docs.python-guide.org/en/latest/dev/virtualenvs/>`_.

Install the latest distributed package
--------------------------------------

You can install the latest distributed package of Pandora by using `pip`::

    $ pip install pandb

Install the development branch
------------------------------

The installation requires that you have `Git <https://git-scm.com/>`_ installed
on your system. Under this prerequisite the first step is to clone the github
repository of Pandora::

    $ git clone https://github.com/frootlab/pandb.git

Thereupon the development branch can locally be installed by using `pip`::

    $ cd pandb
    $ pip install -e .

The ``pip install`` command allows you to follow the development branch as
it changes by creating links in the right places and installing the command
line scripts to the appropriate locations.

Update the development branch
-----------------------------

Once you have cloned the Pandora GitHub repository onto a local directory, you
can update it anytime by running a ``git pull`` in this directory::

    $ git pull

Testing the development branch
------------------------------

Pandora uses the Python builtin package unittest for testing. Since the tests
are not included in the distributed package you are required to install the
Pandora development branch. Thereupon you have to switch to the repository
directory and run::

    $ python3 tests
