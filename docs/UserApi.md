# squacapi_client.UserApi

All URIs are relative to *https://staging-squacapi.pnsn.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create_create**](UserApi.md#user_create_create) | **POST** /user/create/ | 
[**user_groups_create**](UserApi.md#user_groups_create) | **POST** /user/groups/ | 
[**user_groups_delete**](UserApi.md#user_groups_delete) | **DELETE** /user/groups/{id}/ | 
[**user_groups_list**](UserApi.md#user_groups_list) | **GET** /user/groups/ | 
[**user_groups_partial_update**](UserApi.md#user_groups_partial_update) | **PATCH** /user/groups/{id}/ | 
[**user_groups_read**](UserApi.md#user_groups_read) | **GET** /user/groups/{id}/ | 
[**user_groups_update**](UserApi.md#user_groups_update) | **PUT** /user/groups/{id}/ | 
[**user_me_partial_update**](UserApi.md#user_me_partial_update) | **PATCH** /user/me/ | 
[**user_me_read**](UserApi.md#user_me_read) | **GET** /user/me/ | 
[**user_me_update**](UserApi.md#user_me_update) | **PUT** /user/me/ | 
[**user_token_create**](UserApi.md#user_token_create) | **POST** /user/token/ | 


# **user_create_create**
> ReadOnlyUserWriteSerializer user_create_create(data)



create a new user in the system

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from squacapi_client.model.read_only_user_write_serializer import ReadOnlyUserWriteSerializer
from squacapi_client.model.write_only_user_write_serializer import WriteOnlyUserWriteSerializer
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    data = WriteOnlyUserWriteSerializer(
        email="email_example",
        password="password_example",
        firstname="firstname_example",
        lastname="lastname_example",
        groups=[
            1,
        ],
        organization=1,
        is_org_admin=True,
        last_login=dateutil_parser('1970-01-01T00:00:00.00Z'),
        is_active=True,
    ) # WriteOnlyUserWriteSerializer | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_create_create(data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_create_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserWriteSerializer**](WriteOnlyUserWriteSerializer.md)|  |

### Return type

[**ReadOnlyUserWriteSerializer**](ReadOnlyUserWriteSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_create**
> bool, date, datetime, dict, float, int, list, str, none_type user_groups_create(data)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    data = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_groups_create(data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_delete**
> user_groups_delete(id)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.user_groups_delete(id)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_list**
> [dict] user_groups_list()



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.user_groups_list()
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**[dict]**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_partial_update**
> bool, date, datetime, dict, float, int, list, str, none_type user_groups_partial_update(id, data)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 
    data = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_groups_partial_update(id, data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **data** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_read**
> bool, date, datetime, dict, float, int, list, str, none_type user_groups_read(id)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_groups_read(id)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_update**
> bool, date, datetime, dict, float, int, list, str, none_type user_groups_update(id, data)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    id = "id_example" # str | 
    data = {} # bool, date, datetime, dict, float, int, list, str, none_type | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_groups_update(id, data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_groups_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **data** | **bool, date, datetime, dict, float, int, list, str, none_type**|  |

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_partial_update**
> ReadOnlyUserMeSerializer user_me_partial_update(data)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from squacapi_client.model.read_only_user_me_serializer import ReadOnlyUserMeSerializer
from squacapi_client.model.write_only_user_me_serializer import WriteOnlyUserMeSerializer
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    data = WriteOnlyUserMeSerializer(
        password="password_example",
        firstname="firstname_example",
        lastname="lastname_example",
    ) # WriteOnlyUserMeSerializer | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_me_partial_update(data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_me_partial_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserMeSerializer**](WriteOnlyUserMeSerializer.md)|  |

### Return type

[**ReadOnlyUserMeSerializer**](ReadOnlyUserMeSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_read**
> ReadOnlyUserMeSerializer user_me_read()



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from squacapi_client.model.read_only_user_me_serializer import ReadOnlyUserMeSerializer
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.user_me_read()
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_me_read: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ReadOnlyUserMeSerializer**](ReadOnlyUserMeSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_update**
> ReadOnlyUserMeSerializer user_me_update(data)



Manage the authenticated user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from squacapi_client.model.read_only_user_me_serializer import ReadOnlyUserMeSerializer
from squacapi_client.model.write_only_user_me_serializer import WriteOnlyUserMeSerializer
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    data = WriteOnlyUserMeSerializer(
        password="password_example",
        firstname="firstname_example",
        lastname="lastname_example",
    ) # WriteOnlyUserMeSerializer | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_me_update(data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_me_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserMeSerializer**](WriteOnlyUserMeSerializer.md)|  |

### Return type

[**ReadOnlyUserMeSerializer**](ReadOnlyUserMeSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token_create**
> Token user_token_create(data)



create a new auth token for user

### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import user_api
from squacapi_client.model.auth_token import AuthToken
from squacapi_client.model.token import Token
from pprint import pprint
# Defining the host is optional and defaults to https://staging-squacapi.pnsn.org
# See configuration.py for a list of all supported configuration parameters.
configuration = squacapi_client.Configuration(
    host = "https://staging-squacapi.pnsn.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with squacapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    data = AuthToken(
        email="email_example",
        password="password_example",
    ) # AuthToken | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.user_token_create(data)
        pprint(api_response)
    except squacapi_client.ApiException as e:
        print("Exception when calling UserApi->user_token_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**AuthToken**](AuthToken.md)|  |

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

