#!/usr/bin/env bash
# Usage:
#   checkout a branch then run. 
# 	TOKEN=supersecret ./generate_swagger.sh
# To get token go to https://squacapi.pnsn.org/v1.0/user/token/
# to see a list of generate args
#TOKEN=supersecrettoken docker run -v ${PWD}:/tmp --rm swaggerapi/swagger-codegen-cli help generate
docker run -it -v ${PWD}:/local/ --rm "parsertongue/swagger-codegen-cli:latest" \
		generate \
		-i https://staging-squacapi.pnsn.org/swagger.json \
		-l python \
		-c /local/config.json \
		-o /local \
		-a "Authorization: Token $TOKEN"
#mv ./squacapi_client/api/_api.py ./squacapi_client/api/default_api.py
# sed -i '' 's/http:\/\/squacapi/https:\/\/squacapi/g' ./squacapi_client/configuration.py
