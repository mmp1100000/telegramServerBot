#!/bin/bash

git fetch --all
git reset --hard origin/$1

pipenv lock --requirements > requirements.txt
sudo docker-compose up --build
chmod +x deploy.sh