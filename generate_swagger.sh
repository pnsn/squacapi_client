#!/usr/bin/env bash
# Usage: to update, checkout a branch then run. 
# to see a list of generate args
# docker run -v ${PWD}:/tmp --rm swaggerapi/swagger-codegen-cli help generate
docker run -v ${PWD}:/local/ --rm swaggerapi/swagger-codegen-cli \
	generate \
		-i https://squacapi.pnsn.org/swagger.json \
		-l python \
		-c /local/config.json \
		-o /local 
mv ./squacapi_client/api/_api.py ./squacapi_client/api/default_api.py
sed -i '' 's/http:\/\/squacapi/https:\/\/squacapi/g' ./squacapi_client/configuration.py
