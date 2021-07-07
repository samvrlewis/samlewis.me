#!/bin/bash

#report to console
set -e

sudo apt-get -y install pelican

#make the website
pelican  content -o output -s pelicanconf.py

#clean old master dir
rm -rf master

git clone https://github.com/samvrlewis/samvrlewis.github.io.git master

#copy to master
cp -R output/* master

cd master
git config user.email "sam.vr.lewis@gmail.com"
git config user.name "Sam Lewis"
git add -A .
git commit -a -m "Actions #$GITHUB_RUN_ID"

#hide the output so token isn't leaked
git push origin master
