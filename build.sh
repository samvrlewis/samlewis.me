#!/bin/bash

#report to console
set -e

sudo apt-get -y install pelican

#make the website
pelican  content -o output -s pelicanconf.py
