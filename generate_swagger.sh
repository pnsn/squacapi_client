#!/usr/bin/env bash
# Usage:
#   checkout a branch then run. 
# 	TOKEN=supersecret HOST=https://squacapi.pnsn.org/swagger.json ./generate_swagger.sh
# To get token go to https://squacapi.pnsn.org/v1.0/user/token/
# to see a list of generate args
echo $HOST
docker run -it -v ${PWD}:/local/ --rm "parsertongue/swagger-codegen-cli:latest" \
		generate \
		-i $HOST/swagger.json \
		-l python \
		-c /local/config.json \
		-o /local \
		-a "Authorization: Token $TOKEN"

sed -i '' 's/http:\/\/squacapi/https:\/\/squacapi/g' ./squacapi_client/configuration.py
#remove trailing slash
sed -i '' 's/squacapi.pnsn.org\//squacapi.pnsn.org/g' ./squacapi_client/configuration.py
# check configuration.py to make sure host doesn't have trailing /
# Docker image for swaggerapi/swagger-codegen-cli doesn't run on M1 mac
