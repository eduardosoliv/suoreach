import cherrypy

class Dashboard:
    @cherrypy.expose
    def index(self):
        return "Dashboard!"
