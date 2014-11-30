# -*- coding: utf-8 -*-

import os
import json

from flask import Flask, request, session, render_template
from flask import Blueprint, session, make_response, request, current_app
from flask.ext.babel import Babel

from .config import DefaultConfig

# from .utils import INSTANCE_FOLDER_PATH

# App blueprints
from aminer.api.views import api


# For import *
__all__ = ['create_app']

DEFAULT_BLUEPRINTS = [
    api
]


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = DefaultConfig.PROJECT
    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(app_name)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app, blueprints)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(DefaultConfig)

    # http://flask.pocoo.org/docs/config/#instance-folders
    # app.config.from_pyfile('production.cfg', silent=True)

    if config:
        app.config.from_object(config)

        # Use instance folder instead of env variables to make deployment easier.
        # app.config.from_envvar('%s_APP_CONFIG' % DefaultConfig.PROJECT.upper(), silent=True)


def configure_blueprints(app, blueprints):
    """Configure blueprints in views."""
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_hook(app):
    @app.before_request
    def before_request():
        pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_page(error):
        return json.dumps({"status": 403, "message": "forbidden page"}), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return json.dumps({"status": 404, "message": "page not found"}), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return json.dumps({"status": 500, "message": "server error"}), 500

