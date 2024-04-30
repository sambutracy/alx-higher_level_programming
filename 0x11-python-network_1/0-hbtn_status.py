#!/usr/bin/python3
"""
Module to fetch and display status from a URL using urllib
"""

import urllib.request

def fetch_url_status(url):
    """
    Fetches the status of a URL using urllib

    Args:
        url (str): The URL to fetch status from

    Returns:
        str: The status information
    """
    with urllib.request.urlopen(url) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')
        return utf8_content

def display_status():
    """
    Displays the status of the URL
    """
    url = "https://alx-intranet.hbtn.io/status"
    body_response = fetch_url_status(url)
    print("Body response:")
    print("    - type:", type(body_response))
    print("    - content:", repr(body_response))
    print("    - utf8 content:", body_response)

if __name__ == "__main__":
    display_status()
