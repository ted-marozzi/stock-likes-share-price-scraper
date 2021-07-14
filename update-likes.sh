#!/usr/bin/env bash
# Filename: update-likes.sh

cd /home/pi/code/python/pointsbet-likes
git pull --force
python3 ./stockscrape.py

git add -A

git commit -m "Updated likes"
git push
git push
git push
