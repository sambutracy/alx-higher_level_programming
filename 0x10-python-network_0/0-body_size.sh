#!/bin/bash
#This script displays the size of the response in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'

