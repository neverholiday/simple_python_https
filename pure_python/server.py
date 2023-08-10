#!/usr/bin/env python3

import json

from http import HTTPStatus

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

import ssl

from config import ServerConfig

class MainHandler( BaseHTTPRequestHandler ):
	''' This class will be main handler
	'''

	def __init__(self, request, 
						client_address, 
						server ) -> None:
		super().__init__( request, client_address, server )

	def do_GET( self ):
		''' GET method
		'''

		# mock up response dict
		responseDict = {
			'status' : 0
		}

		# dump to str
		responseStr = json.dumps( responseDict, indent=4 )

		# write to file

		
		# send response OK
		self.send_response( HTTPStatus.OK )

		self.send_header( "Content-Type", "application/json" )
		self.end_headers()
		self.wfile.write( responseStr.encode() )
		self.wfile.flush()

def main():
	''' Main function of code
	'''

	# get server config
	serverHost = ServerConfig.ServerHost
	serverPort = ServerConfig.ServerPort
	
	serverCert = ServerConfig.ServerCert 
	serverKey = ServerConfig.ServerKey
	serverCA = ServerConfig.ServerCA

	with HTTPServer( ( serverHost, serverPort ), MainHandler ) as httpServer:
		
		# ssl 
		sslContext = ssl.create_default_context( ssl.Purpose.CLIENT_AUTH, cafile=serverCA )
		sslContext.load_cert_chain( serverCert, serverKey )
		
		# wrap socket
		httpServer.socket = sslContext.wrap_socket( httpServer.socket, server_side=True )
		
		try:
			httpServer.serve_forever()
		except KeyboardInterrupt:
			print( 'Interrupt! exit..' )

if __name__ == '__main__':
	main()


