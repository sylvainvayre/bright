=================================
Welcome to BriPy's documentation!
=================================
BriPy (*Br-eye Pie*), or Bright/Python, is a set of Python bindings for the Bright nuclear fuel cycle model.
Bright is a pure C++ library that models many canonical components such as reactors, 
storage facilities, and more.  These components are then linked to one another using 
a Mass Stream object.  Lastly, an isotopic naming module is available that conveniently 
converts between several standard nuclide naming schemes. 

Arbitrarily hooking together fuel cycle objects in C-code is usually an unwieldy task that 
has low computational overhead.  Bright, therefore, is simply a collection of object models that 
allow another program to connect them.  The BriPy bindings enable this hooking to be done 
in Python.  Thus by using BriPy, Python itself becomes the fuel cycle interpreter while allowing the 
heavy lifting of the models to be performed by the faster C++ code.

Since Bright fuel cycle objects will usually be called via Python, this documentation 
serves for both the Bright objects and BriPy interface.

Bright currently has the following dependencies:
   #. `HDF5 <http://www.hdfgroup.org/HDF5/>`_
   #. `Boost <http://www.boost.org/>`_

BriPy requires these additional dependencies:
   #. `Boost::Python <http://www.boost.org/doc/libs/release/libs/python/doc/>`_
   #. `NumPy <http://numpy.scipy.org/>`_
   #. `SciPy <http://www.scipy.org/>`_
   #. `MatPlotLib <http://matplotlib.sourceforge.net/>`_
   #. `PyTables <http://www.pytables.org/>`_

The source code for Bright and BriPy may be found at the 
`Launchpad project site <http://launchpad.net/bright>`_.
Or you may simply branch from the trunk using bazaar::

    bzr branch lp:bright

--------
Contents
--------

.. toctree::
    :maxdepth: 2

    isoname   
    MassStream
    BriPy

=============
Helpful Links
=============
	
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
