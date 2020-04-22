# squacapi_client.UserApi

All URIs are relative to *http://squacapi.pnsn.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_create_create**](UserApi.md#user_create_create) | **POST** /user/create/ | 
[**user_me_partial_update**](UserApi.md#user_me_partial_update) | **PATCH** /user/me/ | 
[**user_me_read**](UserApi.md#user_me_read) | **GET** /user/me/ | 
[**user_me_update**](UserApi.md#user_me_update) | **PUT** /user/me/ | 
[**user_token_create**](UserApi.md#user_token_create) | **POST** /user/token/ | 


# **user_create_create**
> ReadOnlyUserSerializer user_create_create(data)



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
data = squacapi_client.WriteOnlyUserSerializer() # WriteOnlyUserSerializer | 

try:
    api_response = api_instance.user_create_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_create_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserSerializer**](WriteOnlyUserSerializer.md)|  | 

### Return type

[**ReadOnlyUserSerializer**](ReadOnlyUserSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_partial_update**
> ReadOnlyUserSerializer user_me_partial_update(data)



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
data = squacapi_client.WriteOnlyUserSerializer() # WriteOnlyUserSerializer | 

try:
    api_response = api_instance.user_me_partial_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_me_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserSerializer**](WriteOnlyUserSerializer.md)|  | 

### Return type

[**ReadOnlyUserSerializer**](ReadOnlyUserSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_read**
> ReadOnlyUserSerializer user_me_read()



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

[**ReadOnlyUserSerializer**](ReadOnlyUserSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_update**
> ReadOnlyUserSerializer user_me_update(data)



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
data = squacapi_client.WriteOnlyUserSerializer() # WriteOnlyUserSerializer | 

try:
    api_response = api_instance.user_me_update(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_me_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserSerializer**](WriteOnlyUserSerializer.md)|  | 

### Return type

[**ReadOnlyUserSerializer**](ReadOnlyUserSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_token_create**
> Token user_token_create(data)



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
data = squacapi_client.AuthToken() # AuthToken | 

try:
    api_response = api_instance.user_token_create(data)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

