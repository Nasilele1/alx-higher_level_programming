#!/bin/bash
# Bash script that takes in a URL, sends a GET request to the URL, 
# and displays the body of the response
curl -s -w "\n%{http_code}" "$1" | awk '/^200$/{flag=1;next}flag'
