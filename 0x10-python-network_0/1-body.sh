#!/bin/bash
# Send a get request and display body.
curl -s  -w "%{http_code}" "{$1}" | awk 'NR>1 {print} END {if ($1 == 200) print}'
