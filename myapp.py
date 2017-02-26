import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        raise cherrypy.HTTPRedirect('/dashboard')

class Dashboard(object):
    @cherrypy.expose
    def index(self):
        return "Dashboard!"

class Notes(object):
    @cherrypy.expose
    def index(self):
        return "Notes!"

if __name__ == '__main__':
   cherrypy.config.update("server.conf")
   cherrypy.tree.mount(Root(), '/')
   cherrypy.tree.mount(Dashboard(), '/dashboard')
   cherrypy.tree.mount(Notes(), '/notes')

   cherrypy.engine.start()
   cherrypy.engine.block()
