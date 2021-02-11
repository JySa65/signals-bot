#!/bin/bash

set -o errexit
set -o nounset
set -e

./manage.py runserver 0.0.0.0:8000
