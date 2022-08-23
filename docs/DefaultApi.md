# squacapi_client.DefaultApi

All URIs are relative to *https://staging-squacapi.pnsn.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](DefaultApi.md#list) | **GET** / | 


# **list**
> list()



### Example

* Api Key Authentication (Token):

```python
import time
import squacapi_client
from squacapi_client.api import default_api
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
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_instance.list()
    except squacapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

