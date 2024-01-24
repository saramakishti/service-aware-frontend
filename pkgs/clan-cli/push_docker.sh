#!/usr/bin/env bash

# shellcheck shell=bash
set -euo pipefail

docker login git.tu-berlin.de:5000
docker load < result
docker image tag clan-docker:latest git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest
docker image push git.tu-berlin.de:5000/internet-of-services-lab/service-aware-network-front-end:latest