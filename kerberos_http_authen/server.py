#!/usr/bin/env python3

import os

from flask import Flask
from flask import request
from flask import Response

import requests as pyrequest

from flask import redirect

import kerberos

os.environ[ 'KRB5_KTNAME' ] = 'test_alhambra.keytab'

app = Flask( __name__ )

ServiceName = 'HTTP@test.alhambra.local'


def initkerberosAuthen():
	principalName = kerberos.getServerPrincipalDetails( 'HTTP', 'test.alhambra.local' )
	print( 'principalName = {}'.format( principalName ) )

def _unauthorize():
	return Response('Unauthorized', 401, {'WWW-Authenticate': 'Negotiate'})

@app.route( '/' )
def main():
	return "Who are you ?"

@app.route( '/auth' )
def authen():
	print( '========================================================' )
	header = request.headers.get( "Authorization" ) or request.headers.get( 'WWW-Authenticate' )
	print( f'header = {header}' )
	print( '========================================================' )
	if not header:
		return _unauthorize()
	else:
		token = ''.join(header.split()[1:])
		print( 'token = {}'.format( token ) )
		rc, state = kerberos.authGSSServerInit(ServiceName)
		rc = kerberos.authGSSServerStep(state, token)

		kerberosToken = kerberos.authGSSServerResponse(state)
		user = kerberos.authGSSServerUserName(state)

		if state:
			kerberos.authGSSServerClean(state)
		
		header_ret = { 'WWW-Authenticate' : 'negotiate {}'.format( kerberosToken ) }

		return Response( user, 200,  header_ret )

@app.route( '/test' )
def test():
	print( '========================================================' )
	print( request.headers )
	print( request.url )
	print( '========================================================' )

	return Response( 'Test route', 200 )

if __name__ == '__main__':
	initkerberosAuthen()
	app.run( host='0.0.0.0', port=1111 )