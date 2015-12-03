from webserver import application
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
  http_server = HTTPServer(WSGIContainer(application))
  http_server.listen(7000)
  IOLoop.instance().start()