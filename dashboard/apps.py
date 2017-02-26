import cherrypy

from . import controllers

class Dashboard:
    def __init__(self):
        cherrypy.tree.mount(controllers.Dashboard(), '/dashboard')
