#!/usr/bin/env python3
# Sesheta
# Copyright(C) 2018 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


"""This will handle all the GitHub webhooks."""

import os
from flask import Flask


from .utils import notify_channel, mattermost_username_by_github_user

from .webhooks import webhooks
from .metrics import metrics
from .humans import website


__name__ = 'sesheta'
__version__ = '2.0.0-dev'
__author__ = 'Christoph Görn <goern@redhat.com>'


def create_application():
    """Create, configure and return the Flask application."""
    app = Flask(__name__)
    app.config['SESHETA_GITHUB_WEBHOOK_SECRET'] = os.environ.get(
        'KEBECHET_GITHUB_WEBHOOK_SECRET')
    app.register_blueprint(webhooks)
    app.register_blueprint(metrics)
    app.register_blueprint(website)

    return(app)