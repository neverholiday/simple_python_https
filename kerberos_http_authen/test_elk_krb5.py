#!/usr/bin/env python3

import kerberos
import requests

response = requests.get( 'https://test.alhambra.local:9200/', verify=False )
print( response )
print( response.headers )
print( response.content )

KerberosPrinciple = 'HTTP@test.alhambra.local'

returnCode, krb_context = kerberos.authGSSClientInit( KerberosPrinciple )
kerberos.authGSSClientStep( krb_context, "" )
negotiateDetail = kerberos.authGSSClientResponse( krb_context )


print( '=================================================================' )
headers = {"Authorization": "Negotiate " + negotiateDetail}
response = requests.get( 'https://test.alhambra.local:9200/_plugins/_security/authinfo', verify=False, headers=headers )
print( '\n\n' )
print( dir(response) )
print( response.cookies.keys() )
print( response.headers.get( 'WWW-Authenticate' )  )
print( response.json() )
print( '=================================================================' )

returnCode, krb_context = kerberos.authGSSClientInit( KerberosPrinciple )
kerberos.authGSSClientStep( krb_context, "" )
negotiateDetail = kerberos.authGSSClientResponse( krb_context )


print( '=================================================================' )
headers = {"Authorization": "Negotiate " + negotiateDetail}
response = requests.get( 'https://test.alhambra.local:9200/_plugins/_security/authinfo', verify=False, headers=headers )
print( '\n\n' )
print( dir(response) )
print( response.cookies.keys() )
print( response.headers.get( 'WWW-Authenticate' )  )
print( response.json() )
print( '=================================================================' )

# print( '=================================================================' )
# headers = {"Authorization": "Negotiate " + negotiateDetail}
# response = requests.get( 'https://test.alhambra.local:9200', verify=False, headers=headers )
# print( '\n\n' )
# print( dir(response) )
# print( response.cookies.keys() )
# print( response.headers.get( 'WWW-Authenticate' )  )
# print( response.json() )
# print( '=================================================================' )

# headers = { "WWW-Authenticate": "Negotiate " + negotiateDetail }
# response = requests.get( 'https://test.alhambra.local:9200/_plugins/_security/authinfo', verify=False, headers=headers )
# print( response )
# print( response.headers )
# print( response.content )

