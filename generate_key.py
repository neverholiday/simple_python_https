#!/usr/bin/env python

from cryptography import fernet
from cryptography.fernet import Fernet

secretKey = Fernet.generate_key()
print( secretKey )