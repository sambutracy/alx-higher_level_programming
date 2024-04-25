#!/bin/bash
# Sends a request to the URL and displays only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
