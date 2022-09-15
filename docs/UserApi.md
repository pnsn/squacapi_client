# squacapi_client.UserApi

All URIs are relative to *https://staging-squacapi.pnsn.org/*

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
> ReadOnlyUserWriteSerializer user_create_create(body)



create a new user in the system

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserWriteSerializer() # WriteOnlyUserWriteSerializer | 

try:
    api_response = api_instance.user_create_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_create_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserWriteSerializer**](WriteOnlyUserWriteSerializer.md)|  | 

### Return type

[**ReadOnlyUserWriteSerializer**](ReadOnlyUserWriteSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_create**
> ReadOnlyUserGroupSerializer user_groups_create(body)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 

try:
    api_response = api_instance.user_groups_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 

### Return type

[**ReadOnlyUserGroupSerializer**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_delete**
> user_groups_delete(id)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_instance.user_groups_delete(id)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_list**
> list[ReadOnlyUserGroupSerializer] user_groups_list()



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))

try:
    api_response = api_instance.user_groups_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReadOnlyUserGroupSerializer]**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_partial_update**
> ReadOnlyUserGroupSerializer user_groups_partial_update(body, id)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 
id = 'id_example' # str | 

try:
    api_response = api_instance.user_groups_partial_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 
 **id** | **str**|  | 

### Return type

[**ReadOnlyUserGroupSerializer**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_read**
> ReadOnlyUserGroupSerializer user_groups_read(id)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
id = 'id_example' # str | 

try:
    api_response = api_instance.user_groups_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ReadOnlyUserGroupSerializer**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_update**
> ReadOnlyUserGroupSerializer user_groups_update(body, id)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 
id = 'id_example' # str | 

try:
    api_response = api_instance.user_groups_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 
 **id** | **str**|  | 

### Return type

[**ReadOnlyUserGroupSerializer**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_partial_update**
> ReadOnlyUserMeSerializer user_me_partial_update(body)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserMeSerializer() # WriteOnlyUserMeSerializer | 

try:
    api_response = api_instance.user_me_partial_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_me_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserMeSerializer**](WriteOnlyUserMeSerializer.md)|  | 

### Return type

[**ReadOnlyUserMeSerializer**](ReadOnlyUserMeSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_read**
> ReadOnlyUserMeSerializer user_me_read()



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))

try:
    api_response = api_instance.user_me_read()
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_update**
> ReadOnlyUserMeSerializer user_me_update(body)



Manage the authenticated user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyUserMeSerializer() # WriteOnlyUserMeSerializer | 

try:
    api_response = api_instance.user_me_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_me_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyUserMeSerializer**](WriteOnlyUserMeSerializer.md)|  | 

### Return type

[**ReadOnlyUserMeSerializer**](ReadOnlyUserMeSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token_create**
> Token user_token_create(body)



create a new auth token for user

### Example
```python
from __future__ import print_function
import time
import squacapi_client
from squacapi_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi_client.UserApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.AuthToken() # AuthToken | 

try:
    api_response = api_instance.user_token_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_token_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthToken**](AuthToken.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

