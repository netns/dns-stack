#!/usr/bin/env bash

url="https://www.internic.net/domain/named.root"
output="named.root"

if [ "$(command -v curl)" ]; then
    curl -fsSL -o "$output" "$url"
elif [ "$(command -v wget)" ]; then
    wget -qO "$output" "$url"
else
    echo "error: neither curl or wget found." >&2
    exit 1
fi
