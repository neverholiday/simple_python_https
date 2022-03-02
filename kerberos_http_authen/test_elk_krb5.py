#!/usr/bin/env python3

import kerberos
import requests


KerberosPrinciple = 'HTTP@test.alhambra.local'


returnCode, krb_context = kerberos.authGSSClientInit( KerberosPrinciple )
kerberos.authGSSClientStep( krb_context, "" )
negotiateDetail = kerberos.authGSSClientResponse( krb_context )

headers = {"Authorization": "Negotiate " + negotiateDetail}

response = requests.get( 'https://test.alhambra.local:9200/', verify=False, headers=headers )
# response = requests.get( 'https://test.alhambra.local:9200/', verify=False )
print( response )
print( response.headers )
print( response.content )

