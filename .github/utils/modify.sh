#!/usr/bin/env bash

# Setup user
git config user.name "GitHub Actions Bot"
git config user.email "<>"

# Make random change
echo "abcdefg" >> /code/release-please-test/tmp.txt
git add .
git commit -m 'Added file'
git push


