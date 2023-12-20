#!/usr/bin/bash

PORT=5000
PROCESS=$(lsof -t -i:${PORT})

kill -9 ${PROCESS}
