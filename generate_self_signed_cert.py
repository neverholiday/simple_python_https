#!/usr/bin/env python

from pki_helpers.PkiHelper import PkiHelper

from cryptography import x509
from cryptography.hazmat.backends import default_backend

print( '>> Generate ca-private-key.pem' )
caPrivateKey = PkiHelper.generate_private_key( "ca-private-key.pem", "secret_password" )

print( '>> Generate ca-public-key.pem' )
caPublicKey = PkiHelper.generate_public_key(	caPrivateKey,
												filename="ca-public-key.pem",
												country="US",
												state="Maryland",
												locality="Baltimore",
												org="My CA Company",
												hostname="my-ca.com" )

print( '>> Generate server-private-key.pem' )
server_private_key = PkiHelper.generate_private_key(
	"server-private-key.pem", "a" )

print( '>> Generate server-csr.pem' )
PkiHelper.generate_csr(
	server_private_key,
	filename="server-csr.pem",
	country="US",
	state="Maryland",
	locality="Baltimore",
	org="My Company",
	alt_names=["localhost"],
	hostname="my-site.com",
 )


csr_file = open("server-csr.pem", "rb")
csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())

print( '>> Self signed server-public-key.pem' )
PkiHelper.sign_csr(csr, caPublicKey, caPrivateKey, "server-public-key.pem")
