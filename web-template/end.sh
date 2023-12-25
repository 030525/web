#!/usr/bin/bash

PORT=80
PROCESS=$(lsof -t -i:${PORT})

kill -9 ${PROCESS}
