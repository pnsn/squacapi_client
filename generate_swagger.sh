#!/usr/bin/env bash
docker run -v ${PWD}:/local/ --rm swaggerapi/swagger-codegen-cli \
	generate \
		-i https://squacapi.pnsn.org/swagger.json \
		-l python \
		-c /local/config.json \
		-o /local 
