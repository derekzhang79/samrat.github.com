#!/bin/bash
cd ../syte-pelican; python compress.py; pelican -s settings.py raw; cd - &
