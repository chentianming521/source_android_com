#!/usr/bin/python

import SimpleHTTPServer
import SocketServer
import os

outdir=os.environ.get('OUTDIR', os.getcwd())
os.chdir(outdir)
PORT = int(os.environ.get('HTTP_PORT', 8080))
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(('0.0.0.0', PORT), Handler)
httpd.allow_reuse_address = True
print('Serveing on port %d' % PORT)
httpd.serve_forever()
