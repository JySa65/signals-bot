#!/bin/sh

set -o errexit
set -o nounset


celery -A trading_bot worker -l INFO