#!/usr/bin/env bash
# 1. Dockerfile.base를 사용해서 eb-docker:base 이미지를 생성

#docker build -t eb-docker:base -f Dockerfile.base . &&
#docker tag eb-docker:base docker standbyme227/eb-docker:base

git add -f .secrets && eb deploy --staged --profile=eb; git reset HEAD .secrets