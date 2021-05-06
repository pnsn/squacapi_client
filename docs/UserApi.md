# squacapi_client.UserApi

All URIs are relative to *https://squacapi.pnsn.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_contacts_create**](UserApi.md#user_contacts_create) | **POST** /user/contacts/ | 
[**user_contacts_delete**](UserApi.md#user_contacts_delete) | **DELETE** /user/contacts/{id}/ | 
[**user_contacts_list**](UserApi.md#user_contacts_list) | **GET** /user/contacts/ | 
[**user_contacts_partial_update**](UserApi.md#user_contacts_partial_update) | **PATCH** /user/contacts/{id}/ | 
[**user_contacts_read**](UserApi.md#user_contacts_read) | **GET** /user/contacts/{id}/ | 
[**user_contacts_update**](UserApi.md#user_contacts_update) | **PUT** /user/contacts/{id}/ | 
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
[**user_notifications_create**](UserApi.md#user_notifications_create) | **POST** /user/notifications/ | 
[**user_notifications_delete**](UserApi.md#user_notifications_delete) | **DELETE** /user/notifications/{id}/ | 
[**user_notifications_list**](UserApi.md#user_notifications_list) | **GET** /user/notifications/ | 
[**user_notifications_partial_update**](UserApi.md#user_notifications_partial_update) | **PATCH** /user/notifications/{id}/ | 
[**user_notifications_read**](UserApi.md#user_notifications_read) | **GET** /user/notifications/{id}/ | 
[**user_notifications_update**](UserApi.md#user_notifications_update) | **PUT** /user/notifications/{id}/ | 
[**user_token_create**](UserApi.md#user_token_create) | **POST** /user/token/ | 


# **user_contacts_create**
> ReadOnlyContactSerializer user_contacts_create(data)



Manage contact info

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
data = squacapi_client.WriteOnlyContactSerializer() # WriteOnlyContactSerializer | 

try:
    api_response = api_instance.user_contacts_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyContactSerializer**](WriteOnlyContactSerializer.md)|  | 

### Return type

[**ReadOnlyContactSerializer**](ReadOnlyContactSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_contacts_delete**
> user_contacts_delete(id)



Manage contact info

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
    api_instance.user_contacts_delete(id)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_contacts_list**
> list[ReadOnlyContactSerializer] user_contacts_list()



Manage contact info

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
    api_response = api_instance.user_contacts_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReadOnlyContactSerializer]**](ReadOnlyContactSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_contacts_partial_update**
> ReadOnlyContactSerializer user_contacts_partial_update(id, data)



Manage contact info

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
data = squacapi_client.WriteOnlyContactSerializer() # WriteOnlyContactSerializer | 

try:
    api_response = api_instance.user_contacts_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyContactSerializer**](WriteOnlyContactSerializer.md)|  | 

### Return type

[**ReadOnlyContactSerializer**](ReadOnlyContactSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_contacts_read**
> ReadOnlyContactSerializer user_contacts_read(id)



Manage contact info

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
    api_response = api_instance.user_contacts_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ReadOnlyContactSerializer**](ReadOnlyContactSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_contacts_update**
> ReadOnlyContactSerializer user_contacts_update(id, data)



Manage contact info

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
data = squacapi_client.WriteOnlyContactSerializer() # WriteOnlyContactSerializer | 

try:
    api_response = api_instance.user_contacts_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_contacts_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyContactSerializer**](WriteOnlyContactSerializer.md)|  | 

### Return type

[**ReadOnlyContactSerializer**](ReadOnlyContactSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create_create**
> ReadOnlyUserWriteSerializer user_create_create(data)



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
data = squacapi_client.WriteOnlyUserWriteSerializer() # WriteOnlyUserWriteSerializer | 

try:
    api_response = api_instance.user_create_create(data)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_create**
> ReadOnlyUserGroupSerializer user_groups_create(data)



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
data = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 

try:
    api_response = api_instance.user_groups_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 

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

 - **Content-Type**: application/json
 - **Accept**: application/json

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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_partial_update**
> ReadOnlyUserGroupSerializer user_groups_partial_update(id, data)



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
data = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 

try:
    api_response = api_instance.user_groups_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 

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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_groups_update**
> ReadOnlyUserGroupSerializer user_groups_update(id, data)



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
data = squacapi_client.WriteOnlyUserGroupSerializer() # WriteOnlyUserGroupSerializer | 

try:
    api_response = api_instance.user_groups_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_groups_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyUserGroupSerializer**](WriteOnlyUserGroupSerializer.md)|  | 

### Return type

[**ReadOnlyUserGroupSerializer**](ReadOnlyUserGroupSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_partial_update**
> ReadOnlyUserMeSerializer user_me_partial_update(data)



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
data = squacapi_client.WriteOnlyUserMeSerializer() # WriteOnlyUserMeSerializer | 

try:
    api_response = api_instance.user_me_partial_update(data)
    pprint(api_response)
except ApiException as e:
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_me_update**
> ReadOnlyUserMeSerializer user_me_update(data)



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
data = squacapi_client.WriteOnlyUserMeSerializer() # WriteOnlyUserMeSerializer | 

try:
    api_response = api_instance.user_me_update(data)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_create**
> ReadOnlyNotificationSerializer user_notifications_create(data)



Manage user notifications

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
data = squacapi_client.WriteOnlyNotificationSerializer() # WriteOnlyNotificationSerializer | 

try:
    api_response = api_instance.user_notifications_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**WriteOnlyNotificationSerializer**](WriteOnlyNotificationSerializer.md)|  | 

### Return type

[**ReadOnlyNotificationSerializer**](ReadOnlyNotificationSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_delete**
> user_notifications_delete(id)



Manage user notifications

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
    api_instance.user_notifications_delete(id)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_delete: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_list**
> list[ReadOnlyNotificationDetailSerializer] user_notifications_list()



Manage user notifications

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
    api_response = api_instance.user_notifications_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ReadOnlyNotificationDetailSerializer]**](ReadOnlyNotificationDetailSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_partial_update**
> ReadOnlyNotificationSerializer user_notifications_partial_update(id, data)



Manage user notifications

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
data = squacapi_client.WriteOnlyNotificationSerializer() # WriteOnlyNotificationSerializer | 

try:
    api_response = api_instance.user_notifications_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyNotificationSerializer**](WriteOnlyNotificationSerializer.md)|  | 

### Return type

[**ReadOnlyNotificationSerializer**](ReadOnlyNotificationSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_read**
> ReadOnlyNotificationDetailSerializer user_notifications_read(id)



Manage user notifications

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
    api_response = api_instance.user_notifications_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ReadOnlyNotificationDetailSerializer**](ReadOnlyNotificationDetailSerializer.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_notifications_update**
> ReadOnlyNotificationSerializer user_notifications_update(id, data)



Manage user notifications

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
data = squacapi_client.WriteOnlyNotificationSerializer() # WriteOnlyNotificationSerializer | 

try:
    api_response = api_instance.user_notifications_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_notifications_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data** | [**WriteOnlyNotificationSerializer**](WriteOnlyNotificationSerializer.md)|  | 

### Return type

[**ReadOnlyNotificationSerializer**](ReadOnlyNotificationSerializer.md)

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

