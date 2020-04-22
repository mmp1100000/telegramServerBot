#!/bin/bash

git fetch --all
sudo pipenv lock --requirements > requirements.txt
sudo docker-compose up --build