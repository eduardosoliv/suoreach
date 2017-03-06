import os
import cherrypy
from jinja2 import Environment, PackageLoader

import home.apps
import dashboard.apps

if __name__ == '__main__':
    templates = Environment(loader=PackageLoader('templates', ''))
    cherrypy.config.update("server.conf")
    home.apps.Home()
    dashboard.apps.Dashboard(templates)

    cherrypy.engine.start()
    cherrypy.engine.block()
