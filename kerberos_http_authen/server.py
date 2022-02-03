#!/usr/bin/env python3

import os

from flask import Flask
from flask import request
from flask import Response

import kerberos

os.environ[ 'KRB5_KTNAME' ] = '/data/tmp/test_alhambra.keytab'

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
	header = request.headers.get( "Authorization" )
	# print( f'header = {header}' )
	# print( '========================================================' )
	if not header:
		return _unauthorize()
	else:
		token = ''.join(header.split()[1:])
		rc, state = kerberos.authGSSServerInit(ServiceName)
		rc = kerberos.authGSSServerStep(state, token)

		kerberosToken = kerberos.authGSSServerResponse(state)
		user = kerberos.authGSSServerUserName(state)

		if state:
			kerberos.authGSSServerClean(state)
		
		return Response( user, 200, { 'WWW-Authenticate' : 'negotiate {}'.format( kerberosToken ) } )


if __name__ == '__main__':
	initkerberosAuthen()
	app.run( host='0.0.0.0', port=1111 )