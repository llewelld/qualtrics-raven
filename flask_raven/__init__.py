# -*- coding: utf-8 -*-
"""
    flask_raven
    ~~~~~~~~~~~

    A small library to make authenticating Cambridge students easy
    with flask.

    :copyright: (c) 2014 Daniel Chatfield
    :license: Artistic 2.0
"""

from functools import wraps

from flask import abort, redirect, request, session

from .errors import RavenError
from .helpers import is_auth_request
from .resource import RavenRequest, RavenResponse

__version__ = '0.0.0'
__all__ = ['raven_auth']


def raven_auth():
    def decorator(f):

        @wraps(f)
        def wrapper(*args, **kwargs):

            # Check if this is an authentication request
            if is_auth_request():

                # Cookies are either disabled or not configured properly
                # in flask, we are aborting to prevent a redirect loop
                if '_raven' not in session:
                    abort(403)

                # Auth requests MUST be get requests
                if request.method != 'GET':
                    abort(405)

                if len(request.args.getlist("WLS-Response")) != 1:
                    abort(400)

                raven_response = request.args.get("WLS-Response")

                try:
                    raven_response = RavenResponse(raven_response)
                    return "authenticated"
                except RavenError:
                    abort(405)

            # Check if user is already logged in
            if '_raven' in session and session['_raven'] is not None:
                return f(*args, **kwargs)
            else:
                raven_request = RavenRequest()
                return redirect(raven_request.url, code=303)

        return wrapper
    return decorator
