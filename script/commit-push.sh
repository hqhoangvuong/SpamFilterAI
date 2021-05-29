#!/bin/bash
git push -u origin main
git add .
git commit -m "$1"
git push origin master