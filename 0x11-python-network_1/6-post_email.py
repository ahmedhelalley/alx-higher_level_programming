#!/usr/bin/python3
"""
    Python script that takes in a URL and an email address,
    sends a POST requesed URL with the email as a parameter,
    and finally displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    post_dict = {"email": sys.argv[2]}
    response = requests.post(url, post_dict).text
    print(response)
