#!/bin/bash
# Send GET request to URL passed with custom header, display response body
curl -s -H "X-School-User-Id: 98" "$1"
