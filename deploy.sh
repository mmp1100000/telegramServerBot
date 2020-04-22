#!/bin/bash

git fetch --all
git reset --hard origin/$1

pipenv lock --requirements > requirements.txt
sudo docker-compose up --build $2
chmod +x deploy.sh