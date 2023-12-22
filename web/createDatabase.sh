#!/usr/bin/bash

export FLASK_APP=flaskr
export FLASK_ENV=development

source pj/bin/activate
flask database
