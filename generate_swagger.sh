#!/usr/bin/env bash
# Usage:
#   checkout a branch then run. 
# 	TOKEN=supersecret ./generate_swagger.sh
# To get token go to https://squacapi.pnsn.org/v1.0/user/token/
# to see a list of generate args
#TOKEN=supersecrettoken docker run -v ${PWD}:/tmp --rm swaggerapi/swagger-codegen-cli help generate
echo "Select squacapi host: "
HOST=""

select STAGE in  "production" "staging" "local"
do
  case $STAGE in
		"production")
			HOST="https://squacapi.pnsn.org"
			break ;;

		"staging")
			HOST="https://staging-squacapi.pnsn.org"
			break ;;

		"local")
			HOST="localhost:8000"
			break ;;

		*)
			exit 0
			;;
	esac
done

read -p "Enter token for $STAGE: " TOKEN

docker run -it --platform linux/amd64 \
		-v "${PWD}":/local/ \
		openapitools/openapi-generator-cli generate \
		-i $HOST/swagger.json \
		-g python \
		-c /local/config.json \
		-o /local \
		-a "Authorization: Token $TOKEN"
		


#mv ./squacapi_client/api/_api.py ./squacapi_client/api/default_api.py
sed -i '' 's/http:\/\/squacapi/https:\/\/squacapi/g' ./squacapi_client/configuration.py
