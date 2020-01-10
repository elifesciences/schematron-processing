#!/bin/bash
set -e # everything must succeed.

. download-schematron-rules.sh

. mkvenv.sh

source venv/bin/activate
pip install -r requirements.txt
