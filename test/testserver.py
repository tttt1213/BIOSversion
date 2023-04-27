#!/bin/python3
from http.server import HTTPServer, CGIHTTPRequestHandler

#CGI ハンドラの設定
httpd = HTTPServer(("0.0.0.0", 8888), CGIHTTPRequestHandler)
httpd.serve_forever()
