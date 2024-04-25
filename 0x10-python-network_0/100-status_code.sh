#!/bin/bash
# sends a request and returns the status code
curl -s -o /dev/null -w "%{http_code}" "$1" 
