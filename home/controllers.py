import cherrypy

class Home:
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/dashboard')
