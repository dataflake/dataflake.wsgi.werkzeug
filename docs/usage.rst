Using this package
==================

Using the PasteDeploy entry point
---------------------------------
You can use the PasteDeploy entry point in your WSGI configuration file to
define a ``werkzeug`` server:

.. code-block:: ini

   [server:main]
   use = egg:dataflake.wsgi.werkzeug#main
   host = 127.0.0.1
   port = 8080

If you leave out the ``host`` specification, ``werkzeug``  will listen on all
IPv4 interfaces (`0.0.0.0`). The default port, if none is given, is 8080.

``werkzeug`` supports a wide range of configuration options that you can pass as
part of your WSGI configuration. Here's an example showing all options:

.. code-block:: ini

   [server:main]
   use = egg:dataflake.wsgi.werkzeug#main
   hostname = 127.0.0.1
   port = 8080
   use_debugger = true

The possible options are listed in the `werkzeug documentation 
<https://werkzeug.palletsprojects.com/serving/>`_.


Creating a basic WSGI configuration for Zope
--------------------------------------------
This package defines a console script named ``mkwerkzeuginstance`` that works
just like Zope's own ``mkwsgiinstance``. It will ask you for a location, a
username and a password to create a basic Zope instance home with a WSGI
configuration, in this case it will be ``werkzeug``-based as opposed to Zope's
default, ``waitress``.

.. note::

   Just like ``mkwsgiinstance``, the script will not overwrite an existing WSGI
   configuration file at ``etc/zope.ini``. You need to move the existing file
   to the side to get a fresh configuration.

.. code-block:: console

   $ bin/mkwerkzeuginstance
   Please choose a directory in which you'd like to install
   Zope "instance home" files such as database files, configuration
   files, etc.
   
   Directory: .
   Please choose a username and password for the initial user.
   These will be the credentials you use to initially manage
   your new Zope instance.
   
   Username: admin
   Password: (enter password)
   Verify password: (re-enter password)
