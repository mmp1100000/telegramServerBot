#!/bin/bash

git pull
sudo pipenv lock --requirements > requirements.txt
sudo docker-compose up --build