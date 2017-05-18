#!/usr/bin/env bash

mkdir LegionMarket
mkdir LegionMarket/node_modules
python manage.py makemigrations
python manage.py migrate
yarn install
python manage.py loaddata tlmshop.json
python manage.py collectstatic

#python manage.py createsuperuser
