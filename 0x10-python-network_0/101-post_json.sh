#!/bin/bash
# Sends a JSON post request
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1" 

