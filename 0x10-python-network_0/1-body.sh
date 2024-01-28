#!/bin/bash
# Send a get request and display body.
curl -s -w "%{http_code}\n" "$1" | awk 'NR>1' | grep -q '^200$' && curl -s "$1"
