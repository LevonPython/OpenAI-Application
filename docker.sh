#!/bin/bash

if ! command -v docker &> /dev/null; then
    echo "$0 docker command does not exist, maybe you need to open docker application"
    exit 1;
fi

docker build -t gcr.io/openaiapp2023/openai-app:1 . || exit 1;

docker push gcr.io/openaiapp2023/openai-app:1 || exit 1;

gcloud run deploy --image gcr.io/openaiapp2023/openai-app:1 --platform managed || exit 1;

