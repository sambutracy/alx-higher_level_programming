#!/bin/bash
# This script takes a URL as input, sends a request,
#and displays the size of the response body in bytes

#Send request to provided URL and display the size of response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

