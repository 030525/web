#!/usr/bin/bash

export FLASK_APP=flaskr
export FLASK_ENV=development
export PORT=5000


flask run --port=${PORT}
