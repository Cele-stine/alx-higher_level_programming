#!/bin/bash
# Request methods supported by a server
curl -s -X OPTIONS -i "$1" | awk -vORS=', ' '/Allow/ {gsub(/,/, ""); for (i=2; i<=NF; i++) print $i}'
