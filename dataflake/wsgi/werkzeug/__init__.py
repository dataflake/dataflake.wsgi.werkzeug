##############################################################################
#
# Copyright (c) 2019 Jens Vagelpohl and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
import logging

from werkzeug.serving import run_simple


def _makeBool(value):
    """ Helper to make boolean out of a .ini value """
    if value is None or value.lower() in ('off', 'false', '0'):
        return False
    return True


def serve_paste(app, global_conf, **kw):
    """ A handler for PasteDeploy-compatible runners.

    Sample minimal .ini configuration:

      [server:main]
      use = egg:dataflake.wsgi.werkzeug#main
      hostname = 127.0.0.1
      port = 8080
      use_debugger = True
    """
    if 'hostname' in kw:
        host = kw.pop('hostname', '0.0.0.0')
    elif 'host' in kw:
        host = kw.pop('host', '0.0.0.0')
    port = int(kw.pop('port', '8080'))

    for key in ('use_reloader', 'use_debugger', 'use_evalex',
                'threaded', 'passthrough_errors'):
        # fix up arguments that should be integers
        if key in kw:
            kw[key] = _makeBool(kw[key])

    for key in ('reloader_interval', 'processes'):
        if key in kw:
            kw[key] = int(kw[key])

    run_simple(host, port, app, **kw)
    return 0
