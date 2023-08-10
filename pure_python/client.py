#!/usr/bin/env python3

import json
import ssl

from http.client import HTTPSConnection

from config import ServerConfig

def main():
	'''
	'''
	# hostname and port
	hostname = ServerConfig.ServerHost
	port = ServerConfig.ServerPort
	caFile = ServerConfig.ServerCA

	# headers
	headers = {
		'Content-Type' : 'application/json'
	}

	# create socket layer
	sslContext = ssl.create_default_context( cafile=caFile )

	# connection
	conn = HTTPSConnection( hostname, port, context=sslContext )
	conn.request( 'GET', '/', headers=headers )

	# get response
	response = conn.getresponse()
	print( response.status, response.reason )
	
	# parse payload
	payloadByte = response.read()
	payload = json.loads( payloadByte )

	print( f'payload = {payload}' )

	# close connection
	conn.close()


if __name__ == '__main__':
	main()
