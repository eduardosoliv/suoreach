import os
import cherrypy

import home.apps
import dashboard.apps

if __name__ == '__main__':
    cherrypy.config.update("server.conf")
    home.apps.Home()
    dashboard.apps.Dashboard()

    cherrypy.engine.start()
    cherrypy.engine.block()
