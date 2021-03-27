"""
Grabbing data from google maps
Author: Niklaas Cotta
"""

import requests
import smtplib

# API key
api_file = open("api-key.txt", "r")
api_key = api_file.read()
api_file.close()