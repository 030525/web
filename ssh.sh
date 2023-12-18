#!/usr/bin/bash

ssh-keygen -t rsa -N ""

cat ~/.ssh/id_rsa.pub

git clone -b master git@github.com:030525/web.git

