#!/usr/bin/env bash
# Usage: to update, checkout a branch then run. 
docker run -v ${PWD}:/local/ --rm swaggerapi/swagger-codegen-cli \
	generate \
		-i https://squacapi.pnsn.org/swagger.json \
		-l python \
		-c /local/config.json \
		-o /local 
mv ./squacapi/api/_api.py ./squacapi/api/default_api.py
sed -i '' 's/http:\/\/squacapi/https:\/\/squacapi/g' ./squacapi/configuration.py
