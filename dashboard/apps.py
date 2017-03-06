import cherrypy

from . import controllers

class Dashboard:
    def __init__(self, templates):
        cherrypy.tree.mount(controllers.Dashboard(templates), '/dashboard')
