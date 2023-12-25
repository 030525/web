#!/usr/bin/bash

export FLASK_APP=flaskr
export FLASK_ENV=development
export PORT=80

nohup flask run --port=${PORT} --host=0.0.0.0 > output 2>&1 &


