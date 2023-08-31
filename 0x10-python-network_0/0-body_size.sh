#!/bin/bash
# This script sends a request to a URL and displays the size of the response body in bytes

URL="$1"
RESPONSE=$(curl -sI "$URL" | grep -i "content-length" | awk '{print $2}')
echo "Size of the response body: $RESPONSE bytes"

