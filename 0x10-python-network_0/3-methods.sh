#!/bin/bash
# Send an OPTIONS request and display allowed HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
