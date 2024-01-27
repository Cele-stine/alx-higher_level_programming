#!/bin/bash
# Take a URL send a request to it and display the size of the content.
curl -sI http://www.google.com | awk '/Content-Length/ {print $2}' | tr -d '/r/n'
