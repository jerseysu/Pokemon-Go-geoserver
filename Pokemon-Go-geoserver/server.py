"""
Jersey Su - 2016/07/16 
From : https://wiki.python.org/moin/BaseHttpServer
"""

import BaseHTTPServer
import time
import sys


HOST_NAME = '192.168.1.109' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8000 # Maybe set this to 9000.
REDIRECTIONS = {"/slashdot/": "http://slashdot.org/",
                "/freshmeat/": "http://freshmeat.net/"}

class RedirectHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

    def do_GET(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        json_format = '{"lat":"-33.8754644187737","lng":"151.211257558649"}'
        s.wfile.write( json_format )

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), RedirectHandler)
    print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)