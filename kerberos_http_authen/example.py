#!/usr/bin/env python3

import os

import kerberos
import requests


#	CHANGE THIS 
#		Keytab path for extract token
os.environ[ 'KRB5_KTNAME' ] = 'test_service.keytab'
#		Principle path
ServiceName = 'servicetest'
HostName = 'test.example.local'
KerberosPrinciple = '{}@{}'.format( ServiceName, HostName )


detail = kerberos.getServerPrincipalDetails( ServiceName, HostName )
print( 'detail = {}'.format( detail ) )

#
#	Generate token
#

returnCode, krb_context = kerberos.authGSSClientInit( KerberosPrinciple )
kerberos.authGSSClientStep( krb_context, "" )
negotiateDetail = kerberos.authGSSClientResponse( krb_context )
kerberos.authGSSClientClean( krb_context )


#
#	Extrack token
#

rc, state = kerberos.authGSSServerInit(KerberosPrinciple)
rc = kerberos.authGSSServerStep(state, negotiateDetail)

kerberosToken = kerberos.authGSSServerResponse(state)
user = kerberos.authGSSServerUserName(state)

if state:
	kerberos.authGSSServerClean(state)

print( 'User request: {}'.format( user ) )
