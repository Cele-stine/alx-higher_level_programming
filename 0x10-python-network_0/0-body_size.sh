#!/bin/bash
# Take a URL send a request to it and display the size of the content.
curl -s "{$1}" | wc -c
