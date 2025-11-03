#!/bin/bash
set -e

if [ "$1" = 'casper' ]; then
  exec casper "$@"
elif [ "$1" = 'casper_harmony' ]; then
  exec casper_harmony "$@"
else
  exec casper_harmony "$@"
fi
