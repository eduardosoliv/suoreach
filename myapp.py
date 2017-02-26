import os
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
    static_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

    root_config = {
        '/static/css': {
            'tools.gzip.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(static_dir, 'css'),
            'tools.gzip.mime_types':['text/css']
        },
        '/static/js': {
            'tools.gzip.on': True,
            'tools.staticdir.on': True,
            'tools.staticdir.dir': os.path.join(static_dir, 'js'),
            'tools.gzip.mime_types':['application/javascript']
        },
        '/favicon.ico': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.join(static_dir, 'favicon.ico')
        },
        '/robots.txt': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': os.path.join(static_dir, 'robots.txt')
        }
    }

    cherrypy.config.update("server.conf")
    cherrypy.tree.mount(Root(), '/', root_config)
    cherrypy.tree.mount(Dashboard(), '/dashboard')
    cherrypy.tree.mount(Notes(), '/notes')

    cherrypy.engine.start()
    cherrypy.engine.block()
