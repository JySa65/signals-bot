#!/bin/sh

set -o errexit
set -o nounset

celery flower -A trading_bot --port=5555 --basic_auth=$FLOWER_AUTH
