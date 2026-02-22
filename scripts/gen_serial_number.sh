#!/usr/bin/env bash

# Serial number format:
# YYYYMMDDnn

serial_date=$(date +"%Y%m%d")

if [[ -z "$1" ]]; then
    echo "${serial_date}01"
else
    echo -n "$serial_date"
    echo "$1"
fi

