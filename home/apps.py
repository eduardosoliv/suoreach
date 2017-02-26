import os
import cherrypy

from . import controllers

class Home:
    def __init__(self):
        static_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'static')

        config = {
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

        cherrypy.tree.mount(controllers.Home(), '/', config)
