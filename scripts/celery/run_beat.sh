#!/bin/sh

set -o errexit
set -o nounset


rm ../../celerybeat.pid &   
celery -A trading_bot beat -l INFO