#!/usr/bin/env bash

SOME_FILE_PATH="${1}"
SAMPLE_STRING="${2}"

python3 /action/main.py -f "${SOME_FILE_PATH}" -s "${SAMPLE_STRING}"
