#!/bin/bash

# takes a url
# send s a request
# returns the size of the body the request

curl -s "$1" | wc -c
