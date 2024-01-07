#!/usr/bin/env bash

while true ; do printf 'HTTP/1.1 200 OK\r\n\r\ncool, thanks' | nc -l -N 127.0.0.1 5555 ; done
