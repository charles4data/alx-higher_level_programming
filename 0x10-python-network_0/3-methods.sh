#!/bin/bash
# displays all HTTP methods allowed by a server
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
