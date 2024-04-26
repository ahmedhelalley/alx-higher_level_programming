#!/bin/bash
# Takes in a URL, sends a risplays the size of the body of the response
curl -s "$1" | wc -c
