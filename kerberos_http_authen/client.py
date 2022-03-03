#!/usr/bin/env python3

import os

import kerberos
import requests

response = requests.get( 'http://test.alhambra.local:1111/auth' )
print( response.headers )
# print( response.json() )

ServiceName = 'HTTP'
HostName = 'test.alhambra.local'
KerberosPrinciple = '{}@{}'.format( ServiceName, HostName )

returnCode, krb_context = kerberos.authGSSClientInit( KerberosPrinciple )
kerberos.authGSSClientStep( krb_context, "" )
negotiateDetail = kerberos.authGSSClientResponse( krb_context )
# x = kerberos.authGSSClientUserName( krb_context )

# print( x )

kerberos.authGSSClientClean( krb_context )



headers = {
	'Authorization' : 'Negotiate {}'.format( negotiateDetail )
}

response = requests.get( 'http://test.alhambra.local:1111/auth', headers=headers )
krbToken = response.headers[ 'WWW-Authenticate' ]
print( krbToken )

