# squacapi_client.InviteApi

All URIs are relative to *https://squacapi.pnsn.org/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invite_invite_create**](InviteApi.md#invite_invite_create) | **POST** /invite/invite/ | 
[**invite_register_create**](InviteApi.md#invite_register_create) | **POST** /invite/register/ | 

# **invite_invite_create**
> ReadOnlyInviteTokenSerializer invite_invite_create(body)



Endpoint to invite an inactive user

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
api_instance = squacapi_client.InviteApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyInviteTokenSerializer() # WriteOnlyInviteTokenSerializer | 

try:
    api_response = api_instance.invite_invite_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->invite_invite_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyInviteTokenSerializer**](WriteOnlyInviteTokenSerializer.md)|  | 

### Return type

[**ReadOnlyInviteTokenSerializer**](ReadOnlyInviteTokenSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_register_create**
> ReadOnlyInviteRegisterSerializer invite_register_create(body)



called when invited user authenticates with token and sets password

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
api_instance = squacapi_client.InviteApi(squacapi_client.ApiClient(configuration))
body = squacapi_client.WriteOnlyInviteRegisterSerializer() # WriteOnlyInviteRegisterSerializer | 

try:
    api_response = api_instance.invite_register_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InviteApi->invite_register_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WriteOnlyInviteRegisterSerializer**](WriteOnlyInviteRegisterSerializer.md)|  | 

### Return type

[**ReadOnlyInviteRegisterSerializer**](ReadOnlyInviteRegisterSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

