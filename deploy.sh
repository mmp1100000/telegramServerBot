#!/bin/bash

git fetch --all
git reset --hard origin/$1

sudo pipenv lock --requirements > requirements.txt
sudo docker-compose up --build