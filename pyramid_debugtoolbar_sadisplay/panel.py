#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
sadisplay in pyramid_debugtoolbar
"""
import pydot
import sadisplay
import sqlalchemy

from sqlalchemy import engine_from_config
from pyramid_debugtoolbar.panels import DebugPanel

_ = lambda x: x


def get_sa_base(request, settings=None):
    if settings is None:
        settings = request.registry.settings
    engine = engine_from_config(settings, 'sqlalchemy.')
    sabase = sqlalchemy.ext.declarative.declarative_base()
    sabase.metadata.reflect(engine)
    return sabase


class SadisplayDebugPanel(DebugPanel):
    """
    debug panel
    """
    name = 'SADisplay'
    has_content = True
    template = 'pyramid_debugtoolbar_sadisplay:templates/base.dbtmako'

    def __init__(self, request):
        self.request = request
        self.data = {}
        self.Base = get_sa_base(request)

    def nav_title(self):
        return _('SADisplay')

    def url(self):
        return ''

    def title(self):
        return _('SADisplay')

    def render_vars(self, request):
        tables = self.Base.metadata.tables.values()
        desc = sadisplay.describe(tables)
        dot_data = sadisplay.dot(desc)
        graph = pydot.graph_from_dot_data(str(dot_data))
        svg_img = graph.create_svg()
        return {'svg_img': svg_img}

    def content(self):
        vars = self.render_vars(self.request)
        return self.render(
            'pyramid_debugtoolbar_sadisplay:templates/base.dbtmako',
            vars, self.request)
