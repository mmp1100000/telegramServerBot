#!/bin/bash

git fetch --all origin/$1
sudo pipenv lock --requirements > requirements.txt
sudo docker-compose up --build