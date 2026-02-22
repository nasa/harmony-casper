#!/bin/bash
set -e

if [ "$1" = 'casper' ]; then
  exec uv run casper "$@"
elif [ "$1" = 'casper_harmony' ]; then
  exec uv run casper_harmony "$@"
else
  exec uv run casper_harmony "$@"
fi
