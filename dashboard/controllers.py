import cherrypy
from jinja2 import Template

class Dashboard:
    def __init__(self, templates):
        self.__templates = templates

    @cherrypy.expose
    def index(self):
        return self.__templates.get_template('dashboard/index.html').render()

    @cherrypy.expose
    def details(self):
        return self.__templates.get_template('dashboard/details.html').render()

    #@cherrypy.expose
    #def edit(self, number):
    #    return self.__templates.get_template('dashboard.html').render(n=number)
