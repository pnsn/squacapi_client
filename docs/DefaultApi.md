# squacapi.DefaultApi

All URIs are relative to *http://squacapi.pnsn.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](DefaultApi.md#list) | **GET** / | 


# **list**
> list()





### Example
```python
from __future__ import print_function
import time
import squacapi
from squacapi.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
configuration = squacapi.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = squacapi.DefaultApi(squacapi.ApiClient(configuration))

try:
    api_instance.list()
except ApiException as e:
    print("Exception when calling DefaultApi->list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

