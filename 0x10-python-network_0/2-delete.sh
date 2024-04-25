#!/bin/bash
#Sends DELETE request to URL passed as first argument and display response body
curl -sX DELETE "$1"
