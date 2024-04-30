#!/usr/bin/python3

"""
Script that fetches https://alx-intranet.hbtn.io/status using requests package
"""

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    body_response = response.text

    print("Body response:")
    print("    - type:", type(body_response))
    print("    - content:", body_response)
