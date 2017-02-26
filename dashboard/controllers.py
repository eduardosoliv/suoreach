import cherrypy

class Dashboard:
    @cherrypy.expose
    def index(self):
        return "Dashboard!"
    @cherrypy.expose
    def edit(self, number):
        return "Dashboard edit " + number
