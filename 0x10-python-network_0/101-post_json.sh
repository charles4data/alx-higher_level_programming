#!/bin/bash
# Sends a JSON post request
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
