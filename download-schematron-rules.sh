#!/bin/bash
# clones/updates the elife api-raml repository
# this repository contains the specification for article-json and
# is used to validate what the scraper generates.
# see `src/validate.py`

set -e # everything must pass
mkdir -p schema
cd schema
if [ ! -d reference ]; then
    git clone https://github.com/elifesciences/reference-schematron reference
fi
cd ..

if [ -f reference.sha1 ]; then
    sha="$(cat reference.sha1)"
    cd schema/reference/
    git reset --hard
    git fetch
    git checkout "$sha"
    cd -
fi
