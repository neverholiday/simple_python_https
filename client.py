#!/usr/bin/env python3

import os
import requests

def getMessage():
	url = 'https://localhost:1234'
	response = requests.get( url, verify="ca-public-key.pem" )
	print( f"The secret message is: {response.text}" )

if __name__ == "__main__":
	getMessage()