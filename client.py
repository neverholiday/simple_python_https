#!/usr/bin/env python3

import os
import requests

def getMessage():
	url = os.environ[ "SECRET_URL" ]
	response = requests.get( url )
	print( f"The secret message is: {response.text}" )

if __name__ == "__main__":
	getMessage()