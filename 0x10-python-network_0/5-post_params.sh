#!/bin/bash
# sends a POST request with parameters and displays response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject= I will always be here for PLD"
