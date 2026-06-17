#!/bin/bash

for i in {1..30};
    do echo "request: $i" && curl -s -i localhost:80; 
done | sed -n '/^served_by/p'