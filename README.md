# squacapi_client
API for accessing squac data

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import squacapi_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import squacapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = squacapi_client.DefaultApi(squacapi_client.ApiClient(configuration))

try:
    api_instance.list()
except ApiException as e:
    print("Exception when calling DefaultApi->list: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://squacapi.pnsn.org*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**list**](docs/DefaultApi.md#list) | **GET** / | 
*UserApi* | [**user_contacts_create**](docs/UserApi.md#user_contacts_create) | **POST** /user/contacts/ | 
*UserApi* | [**user_contacts_delete**](docs/UserApi.md#user_contacts_delete) | **DELETE** /user/contacts/{id}/ | 
*UserApi* | [**user_contacts_list**](docs/UserApi.md#user_contacts_list) | **GET** /user/contacts/ | 
*UserApi* | [**user_contacts_partial_update**](docs/UserApi.md#user_contacts_partial_update) | **PATCH** /user/contacts/{id}/ | 
*UserApi* | [**user_contacts_read**](docs/UserApi.md#user_contacts_read) | **GET** /user/contacts/{id}/ | 
*UserApi* | [**user_contacts_update**](docs/UserApi.md#user_contacts_update) | **PUT** /user/contacts/{id}/ | 
*UserApi* | [**user_create_create**](docs/UserApi.md#user_create_create) | **POST** /user/create/ | 
*UserApi* | [**user_groups_create**](docs/UserApi.md#user_groups_create) | **POST** /user/groups/ | 
*UserApi* | [**user_groups_delete**](docs/UserApi.md#user_groups_delete) | **DELETE** /user/groups/{id}/ | 
*UserApi* | [**user_groups_list**](docs/UserApi.md#user_groups_list) | **GET** /user/groups/ | 
*UserApi* | [**user_groups_partial_update**](docs/UserApi.md#user_groups_partial_update) | **PATCH** /user/groups/{id}/ | 
*UserApi* | [**user_groups_read**](docs/UserApi.md#user_groups_read) | **GET** /user/groups/{id}/ | 
*UserApi* | [**user_groups_update**](docs/UserApi.md#user_groups_update) | **PUT** /user/groups/{id}/ | 
*UserApi* | [**user_me_partial_update**](docs/UserApi.md#user_me_partial_update) | **PATCH** /user/me/ | 
*UserApi* | [**user_me_read**](docs/UserApi.md#user_me_read) | **GET** /user/me/ | 
*UserApi* | [**user_me_update**](docs/UserApi.md#user_me_update) | **PUT** /user/me/ | 
*UserApi* | [**user_notifications_create**](docs/UserApi.md#user_notifications_create) | **POST** /user/notifications/ | 
*UserApi* | [**user_notifications_delete**](docs/UserApi.md#user_notifications_delete) | **DELETE** /user/notifications/{id}/ | 
*UserApi* | [**user_notifications_list**](docs/UserApi.md#user_notifications_list) | **GET** /user/notifications/ | 
*UserApi* | [**user_notifications_partial_update**](docs/UserApi.md#user_notifications_partial_update) | **PATCH** /user/notifications/{id}/ | 
*UserApi* | [**user_notifications_read**](docs/UserApi.md#user_notifications_read) | **GET** /user/notifications/{id}/ | 
*UserApi* | [**user_notifications_update**](docs/UserApi.md#user_notifications_update) | **PUT** /user/notifications/{id}/ | 
*UserApi* | [**user_token_create**](docs/UserApi.md#user_token_create) | **POST** /user/token/ | 
*V10Api* | [**v1_0_dashboard_dashboards_create**](docs/V10Api.md#v1_0_dashboard_dashboards_create) | **POST** /v1.0/dashboard/dashboards/ | 
*V10Api* | [**v1_0_dashboard_dashboards_delete**](docs/V10Api.md#v1_0_dashboard_dashboards_delete) | **DELETE** /v1.0/dashboard/dashboards/{id}/ | 
*V10Api* | [**v1_0_dashboard_dashboards_list**](docs/V10Api.md#v1_0_dashboard_dashboards_list) | **GET** /v1.0/dashboard/dashboards/ | 
*V10Api* | [**v1_0_dashboard_dashboards_partial_update**](docs/V10Api.md#v1_0_dashboard_dashboards_partial_update) | **PATCH** /v1.0/dashboard/dashboards/{id}/ | 
*V10Api* | [**v1_0_dashboard_dashboards_read**](docs/V10Api.md#v1_0_dashboard_dashboards_read) | **GET** /v1.0/dashboard/dashboards/{id}/ | 
*V10Api* | [**v1_0_dashboard_dashboards_update**](docs/V10Api.md#v1_0_dashboard_dashboards_update) | **PUT** /v1.0/dashboard/dashboards/{id}/ | 
*V10Api* | [**v1_0_dashboard_stattype_create**](docs/V10Api.md#v1_0_dashboard_stattype_create) | **POST** /v1.0/dashboard/stattype/ | 
*V10Api* | [**v1_0_dashboard_stattype_delete**](docs/V10Api.md#v1_0_dashboard_stattype_delete) | **DELETE** /v1.0/dashboard/stattype/{id}/ | 
*V10Api* | [**v1_0_dashboard_stattype_list**](docs/V10Api.md#v1_0_dashboard_stattype_list) | **GET** /v1.0/dashboard/stattype/ | 
*V10Api* | [**v1_0_dashboard_stattype_partial_update**](docs/V10Api.md#v1_0_dashboard_stattype_partial_update) | **PATCH** /v1.0/dashboard/stattype/{id}/ | 
*V10Api* | [**v1_0_dashboard_stattype_read**](docs/V10Api.md#v1_0_dashboard_stattype_read) | **GET** /v1.0/dashboard/stattype/{id}/ | 
*V10Api* | [**v1_0_dashboard_stattype_update**](docs/V10Api.md#v1_0_dashboard_stattype_update) | **PUT** /v1.0/dashboard/stattype/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgets_create**](docs/V10Api.md#v1_0_dashboard_widgets_create) | **POST** /v1.0/dashboard/widgets/ | 
*V10Api* | [**v1_0_dashboard_widgets_delete**](docs/V10Api.md#v1_0_dashboard_widgets_delete) | **DELETE** /v1.0/dashboard/widgets/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgets_list**](docs/V10Api.md#v1_0_dashboard_widgets_list) | **GET** /v1.0/dashboard/widgets/ | 
*V10Api* | [**v1_0_dashboard_widgets_partial_update**](docs/V10Api.md#v1_0_dashboard_widgets_partial_update) | **PATCH** /v1.0/dashboard/widgets/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgets_read**](docs/V10Api.md#v1_0_dashboard_widgets_read) | **GET** /v1.0/dashboard/widgets/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgets_update**](docs/V10Api.md#v1_0_dashboard_widgets_update) | **PUT** /v1.0/dashboard/widgets/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_create**](docs/V10Api.md#v1_0_dashboard_widgettypes_create) | **POST** /v1.0/dashboard/widgettypes/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_delete**](docs/V10Api.md#v1_0_dashboard_widgettypes_delete) | **DELETE** /v1.0/dashboard/widgettypes/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_list**](docs/V10Api.md#v1_0_dashboard_widgettypes_list) | **GET** /v1.0/dashboard/widgettypes/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_partial_update**](docs/V10Api.md#v1_0_dashboard_widgettypes_partial_update) | **PATCH** /v1.0/dashboard/widgettypes/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_read**](docs/V10Api.md#v1_0_dashboard_widgettypes_read) | **GET** /v1.0/dashboard/widgettypes/{id}/ | 
*V10Api* | [**v1_0_dashboard_widgettypes_update**](docs/V10Api.md#v1_0_dashboard_widgettypes_update) | **PUT** /v1.0/dashboard/widgettypes/{id}/ | 
*V10Api* | [**v1_0_invite_invite_create**](docs/V10Api.md#v1_0_invite_invite_create) | **POST** /v1.0/invite/invite/ | 
*V10Api* | [**v1_0_invite_register_create**](docs/V10Api.md#v1_0_invite_register_create) | **POST** /v1.0/invite/register/ | 
*V10Api* | [**v1_0_list**](docs/V10Api.md#v1_0_list) | **GET** /v1.0/ | 
*V10Api* | [**v1_0_measurement_aggregated_list**](docs/V10Api.md#v1_0_measurement_aggregated_list) | **GET** /v1.0/measurement/aggregated/ | 
*V10Api* | [**v1_0_measurement_alerts_create**](docs/V10Api.md#v1_0_measurement_alerts_create) | **POST** /v1.0/measurement/alerts/ | 
*V10Api* | [**v1_0_measurement_alerts_delete**](docs/V10Api.md#v1_0_measurement_alerts_delete) | **DELETE** /v1.0/measurement/alerts/{id}/ | 
*V10Api* | [**v1_0_measurement_alerts_list**](docs/V10Api.md#v1_0_measurement_alerts_list) | **GET** /v1.0/measurement/alerts/ | 
*V10Api* | [**v1_0_measurement_alerts_partial_update**](docs/V10Api.md#v1_0_measurement_alerts_partial_update) | **PATCH** /v1.0/measurement/alerts/{id}/ | 
*V10Api* | [**v1_0_measurement_alerts_read**](docs/V10Api.md#v1_0_measurement_alerts_read) | **GET** /v1.0/measurement/alerts/{id}/ | 
*V10Api* | [**v1_0_measurement_alerts_update**](docs/V10Api.md#v1_0_measurement_alerts_update) | **PUT** /v1.0/measurement/alerts/{id}/ | 
*V10Api* | [**v1_0_measurement_day_archives_list**](docs/V10Api.md#v1_0_measurement_day_archives_list) | **GET** /v1.0/measurement/day-archives/ | 
*V10Api* | [**v1_0_measurement_day_archives_read**](docs/V10Api.md#v1_0_measurement_day_archives_read) | **GET** /v1.0/measurement/day-archives/{id}/ | 
*V10Api* | [**v1_0_measurement_hour_archives_list**](docs/V10Api.md#v1_0_measurement_hour_archives_list) | **GET** /v1.0/measurement/hour-archives/ | 
*V10Api* | [**v1_0_measurement_hour_archives_read**](docs/V10Api.md#v1_0_measurement_hour_archives_read) | **GET** /v1.0/measurement/hour-archives/{id}/ | 
*V10Api* | [**v1_0_measurement_measurements_create**](docs/V10Api.md#v1_0_measurement_measurements_create) | **POST** /v1.0/measurement/measurements/ | 
*V10Api* | [**v1_0_measurement_measurements_delete**](docs/V10Api.md#v1_0_measurement_measurements_delete) | **DELETE** /v1.0/measurement/measurements/{id}/ | 
*V10Api* | [**v1_0_measurement_measurements_list**](docs/V10Api.md#v1_0_measurement_measurements_list) | **GET** /v1.0/measurement/measurements/ | 
*V10Api* | [**v1_0_measurement_measurements_partial_update**](docs/V10Api.md#v1_0_measurement_measurements_partial_update) | **PATCH** /v1.0/measurement/measurements/{id}/ | 
*V10Api* | [**v1_0_measurement_measurements_read**](docs/V10Api.md#v1_0_measurement_measurements_read) | **GET** /v1.0/measurement/measurements/{id}/ | 
*V10Api* | [**v1_0_measurement_measurements_update**](docs/V10Api.md#v1_0_measurement_measurements_update) | **PUT** /v1.0/measurement/measurements/{id}/ | 
*V10Api* | [**v1_0_measurement_metrics_create**](docs/V10Api.md#v1_0_measurement_metrics_create) | **POST** /v1.0/measurement/metrics/ | 
*V10Api* | [**v1_0_measurement_metrics_delete**](docs/V10Api.md#v1_0_measurement_metrics_delete) | **DELETE** /v1.0/measurement/metrics/{id}/ | 
*V10Api* | [**v1_0_measurement_metrics_list**](docs/V10Api.md#v1_0_measurement_metrics_list) | **GET** /v1.0/measurement/metrics/ | 
*V10Api* | [**v1_0_measurement_metrics_partial_update**](docs/V10Api.md#v1_0_measurement_metrics_partial_update) | **PATCH** /v1.0/measurement/metrics/{id}/ | 
*V10Api* | [**v1_0_measurement_metrics_read**](docs/V10Api.md#v1_0_measurement_metrics_read) | **GET** /v1.0/measurement/metrics/{id}/ | 
*V10Api* | [**v1_0_measurement_metrics_update**](docs/V10Api.md#v1_0_measurement_metrics_update) | **PUT** /v1.0/measurement/metrics/{id}/ | 
*V10Api* | [**v1_0_measurement_monitors_create**](docs/V10Api.md#v1_0_measurement_monitors_create) | **POST** /v1.0/measurement/monitors/ | 
*V10Api* | [**v1_0_measurement_monitors_delete**](docs/V10Api.md#v1_0_measurement_monitors_delete) | **DELETE** /v1.0/measurement/monitors/{id}/ | 
*V10Api* | [**v1_0_measurement_monitors_list**](docs/V10Api.md#v1_0_measurement_monitors_list) | **GET** /v1.0/measurement/monitors/ | 
*V10Api* | [**v1_0_measurement_monitors_partial_update**](docs/V10Api.md#v1_0_measurement_monitors_partial_update) | **PATCH** /v1.0/measurement/monitors/{id}/ | 
*V10Api* | [**v1_0_measurement_monitors_read**](docs/V10Api.md#v1_0_measurement_monitors_read) | **GET** /v1.0/measurement/monitors/{id}/ | 
*V10Api* | [**v1_0_measurement_monitors_update**](docs/V10Api.md#v1_0_measurement_monitors_update) | **PUT** /v1.0/measurement/monitors/{id}/ | 
*V10Api* | [**v1_0_measurement_month_archives_list**](docs/V10Api.md#v1_0_measurement_month_archives_list) | **GET** /v1.0/measurement/month-archives/ | 
*V10Api* | [**v1_0_measurement_month_archives_read**](docs/V10Api.md#v1_0_measurement_month_archives_read) | **GET** /v1.0/measurement/month-archives/{id}/ | 
*V10Api* | [**v1_0_measurement_thresholds_create**](docs/V10Api.md#v1_0_measurement_thresholds_create) | **POST** /v1.0/measurement/thresholds/ | 
*V10Api* | [**v1_0_measurement_thresholds_delete**](docs/V10Api.md#v1_0_measurement_thresholds_delete) | **DELETE** /v1.0/measurement/thresholds/{id}/ | 
*V10Api* | [**v1_0_measurement_thresholds_list**](docs/V10Api.md#v1_0_measurement_thresholds_list) | **GET** /v1.0/measurement/thresholds/ | 
*V10Api* | [**v1_0_measurement_thresholds_partial_update**](docs/V10Api.md#v1_0_measurement_thresholds_partial_update) | **PATCH** /v1.0/measurement/thresholds/{id}/ | 
*V10Api* | [**v1_0_measurement_thresholds_read**](docs/V10Api.md#v1_0_measurement_thresholds_read) | **GET** /v1.0/measurement/thresholds/{id}/ | 
*V10Api* | [**v1_0_measurement_thresholds_update**](docs/V10Api.md#v1_0_measurement_thresholds_update) | **PUT** /v1.0/measurement/thresholds/{id}/ | 
*V10Api* | [**v1_0_measurement_triggers_create**](docs/V10Api.md#v1_0_measurement_triggers_create) | **POST** /v1.0/measurement/triggers/ | 
*V10Api* | [**v1_0_measurement_triggers_delete**](docs/V10Api.md#v1_0_measurement_triggers_delete) | **DELETE** /v1.0/measurement/triggers/{id}/ | 
*V10Api* | [**v1_0_measurement_triggers_list**](docs/V10Api.md#v1_0_measurement_triggers_list) | **GET** /v1.0/measurement/triggers/ | 
*V10Api* | [**v1_0_measurement_triggers_partial_update**](docs/V10Api.md#v1_0_measurement_triggers_partial_update) | **PATCH** /v1.0/measurement/triggers/{id}/ | 
*V10Api* | [**v1_0_measurement_triggers_read**](docs/V10Api.md#v1_0_measurement_triggers_read) | **GET** /v1.0/measurement/triggers/{id}/ | 
*V10Api* | [**v1_0_measurement_triggers_update**](docs/V10Api.md#v1_0_measurement_triggers_update) | **PUT** /v1.0/measurement/triggers/{id}/ | 
*V10Api* | [**v1_0_measurement_week_archives_list**](docs/V10Api.md#v1_0_measurement_week_archives_list) | **GET** /v1.0/measurement/week-archives/ | 
*V10Api* | [**v1_0_measurement_week_archives_read**](docs/V10Api.md#v1_0_measurement_week_archives_read) | **GET** /v1.0/measurement/week-archives/{id}/ | 
*V10Api* | [**v1_0_nslc_channels_create**](docs/V10Api.md#v1_0_nslc_channels_create) | **POST** /v1.0/nslc/channels/ | 
*V10Api* | [**v1_0_nslc_channels_delete**](docs/V10Api.md#v1_0_nslc_channels_delete) | **DELETE** /v1.0/nslc/channels/{id}/ | 
*V10Api* | [**v1_0_nslc_channels_list**](docs/V10Api.md#v1_0_nslc_channels_list) | **GET** /v1.0/nslc/channels/ | 
*V10Api* | [**v1_0_nslc_channels_partial_update**](docs/V10Api.md#v1_0_nslc_channels_partial_update) | **PATCH** /v1.0/nslc/channels/{id}/ | 
*V10Api* | [**v1_0_nslc_channels_read**](docs/V10Api.md#v1_0_nslc_channels_read) | **GET** /v1.0/nslc/channels/{id}/ | 
*V10Api* | [**v1_0_nslc_channels_update**](docs/V10Api.md#v1_0_nslc_channels_update) | **PUT** /v1.0/nslc/channels/{id}/ | 
*V10Api* | [**v1_0_nslc_groups_create**](docs/V10Api.md#v1_0_nslc_groups_create) | **POST** /v1.0/nslc/groups/ | 
*V10Api* | [**v1_0_nslc_groups_delete**](docs/V10Api.md#v1_0_nslc_groups_delete) | **DELETE** /v1.0/nslc/groups/{id}/ | 
*V10Api* | [**v1_0_nslc_groups_list**](docs/V10Api.md#v1_0_nslc_groups_list) | **GET** /v1.0/nslc/groups/ | 
*V10Api* | [**v1_0_nslc_groups_partial_update**](docs/V10Api.md#v1_0_nslc_groups_partial_update) | **PATCH** /v1.0/nslc/groups/{id}/ | 
*V10Api* | [**v1_0_nslc_groups_read**](docs/V10Api.md#v1_0_nslc_groups_read) | **GET** /v1.0/nslc/groups/{id}/ | 
*V10Api* | [**v1_0_nslc_groups_update**](docs/V10Api.md#v1_0_nslc_groups_update) | **PUT** /v1.0/nslc/groups/{id}/ | 
*V10Api* | [**v1_0_nslc_networks_create**](docs/V10Api.md#v1_0_nslc_networks_create) | **POST** /v1.0/nslc/networks/ | 
*V10Api* | [**v1_0_nslc_networks_delete**](docs/V10Api.md#v1_0_nslc_networks_delete) | **DELETE** /v1.0/nslc/networks/{code}/ | 
*V10Api* | [**v1_0_nslc_networks_list**](docs/V10Api.md#v1_0_nslc_networks_list) | **GET** /v1.0/nslc/networks/ | 
*V10Api* | [**v1_0_nslc_networks_partial_update**](docs/V10Api.md#v1_0_nslc_networks_partial_update) | **PATCH** /v1.0/nslc/networks/{code}/ | 
*V10Api* | [**v1_0_nslc_networks_read**](docs/V10Api.md#v1_0_nslc_networks_read) | **GET** /v1.0/nslc/networks/{code}/ | 
*V10Api* | [**v1_0_nslc_networks_update**](docs/V10Api.md#v1_0_nslc_networks_update) | **PUT** /v1.0/nslc/networks/{code}/ | 
*V10Api* | [**v1_0_organization_organizations_create**](docs/V10Api.md#v1_0_organization_organizations_create) | **POST** /v1.0/organization/organizations/ | 
*V10Api* | [**v1_0_organization_organizations_delete**](docs/V10Api.md#v1_0_organization_organizations_delete) | **DELETE** /v1.0/organization/organizations/{id}/ | 
*V10Api* | [**v1_0_organization_organizations_list**](docs/V10Api.md#v1_0_organization_organizations_list) | **GET** /v1.0/organization/organizations/ | 
*V10Api* | [**v1_0_organization_organizations_partial_update**](docs/V10Api.md#v1_0_organization_organizations_partial_update) | **PATCH** /v1.0/organization/organizations/{id}/ | 
*V10Api* | [**v1_0_organization_organizations_read**](docs/V10Api.md#v1_0_organization_organizations_read) | **GET** /v1.0/organization/organizations/{id}/ | 
*V10Api* | [**v1_0_organization_organizations_update**](docs/V10Api.md#v1_0_organization_organizations_update) | **PUT** /v1.0/organization/organizations/{id}/ | 
*V10Api* | [**v1_0_organization_users_create**](docs/V10Api.md#v1_0_organization_users_create) | **POST** /v1.0/organization/users/ | 
*V10Api* | [**v1_0_organization_users_delete**](docs/V10Api.md#v1_0_organization_users_delete) | **DELETE** /v1.0/organization/users/{id}/ | 
*V10Api* | [**v1_0_organization_users_list**](docs/V10Api.md#v1_0_organization_users_list) | **GET** /v1.0/organization/users/ | 
*V10Api* | [**v1_0_organization_users_partial_update**](docs/V10Api.md#v1_0_organization_users_partial_update) | **PATCH** /v1.0/organization/users/{id}/ | 
*V10Api* | [**v1_0_organization_users_read**](docs/V10Api.md#v1_0_organization_users_read) | **GET** /v1.0/organization/users/{id}/ | 
*V10Api* | [**v1_0_organization_users_update**](docs/V10Api.md#v1_0_organization_users_update) | **PUT** /v1.0/organization/users/{id}/ | 
*V10Api* | [**v1_0_password_reset_confirm_create**](docs/V10Api.md#v1_0_password_reset_confirm_create) | **POST** /v1.0/password_reset/confirm/ | 
*V10Api* | [**v1_0_password_reset_create**](docs/V10Api.md#v1_0_password_reset_create) | **POST** /v1.0/password_reset/ | An Api View which provides a method to request a password reset token based on an e-mail address
*V10Api* | [**v1_0_password_reset_validate_token_create**](docs/V10Api.md#v1_0_password_reset_validate_token_create) | **POST** /v1.0/password_reset/validate_token/ | 
*V10Api* | [**v1_0_user_contacts_create**](docs/V10Api.md#v1_0_user_contacts_create) | **POST** /v1.0/user/contacts/ | 
*V10Api* | [**v1_0_user_contacts_delete**](docs/V10Api.md#v1_0_user_contacts_delete) | **DELETE** /v1.0/user/contacts/{id}/ | 
*V10Api* | [**v1_0_user_contacts_list**](docs/V10Api.md#v1_0_user_contacts_list) | **GET** /v1.0/user/contacts/ | 
*V10Api* | [**v1_0_user_contacts_partial_update**](docs/V10Api.md#v1_0_user_contacts_partial_update) | **PATCH** /v1.0/user/contacts/{id}/ | 
*V10Api* | [**v1_0_user_contacts_read**](docs/V10Api.md#v1_0_user_contacts_read) | **GET** /v1.0/user/contacts/{id}/ | 
*V10Api* | [**v1_0_user_contacts_update**](docs/V10Api.md#v1_0_user_contacts_update) | **PUT** /v1.0/user/contacts/{id}/ | 
*V10Api* | [**v1_0_user_create_create**](docs/V10Api.md#v1_0_user_create_create) | **POST** /v1.0/user/create/ | 
*V10Api* | [**v1_0_user_groups_create**](docs/V10Api.md#v1_0_user_groups_create) | **POST** /v1.0/user/groups/ | 
*V10Api* | [**v1_0_user_groups_delete**](docs/V10Api.md#v1_0_user_groups_delete) | **DELETE** /v1.0/user/groups/{id}/ | 
*V10Api* | [**v1_0_user_groups_list**](docs/V10Api.md#v1_0_user_groups_list) | **GET** /v1.0/user/groups/ | 
*V10Api* | [**v1_0_user_groups_partial_update**](docs/V10Api.md#v1_0_user_groups_partial_update) | **PATCH** /v1.0/user/groups/{id}/ | 
*V10Api* | [**v1_0_user_groups_read**](docs/V10Api.md#v1_0_user_groups_read) | **GET** /v1.0/user/groups/{id}/ | 
*V10Api* | [**v1_0_user_groups_update**](docs/V10Api.md#v1_0_user_groups_update) | **PUT** /v1.0/user/groups/{id}/ | 
*V10Api* | [**v1_0_user_me_partial_update**](docs/V10Api.md#v1_0_user_me_partial_update) | **PATCH** /v1.0/user/me/ | 
*V10Api* | [**v1_0_user_me_read**](docs/V10Api.md#v1_0_user_me_read) | **GET** /v1.0/user/me/ | 
*V10Api* | [**v1_0_user_me_update**](docs/V10Api.md#v1_0_user_me_update) | **PUT** /v1.0/user/me/ | 
*V10Api* | [**v1_0_user_notifications_create**](docs/V10Api.md#v1_0_user_notifications_create) | **POST** /v1.0/user/notifications/ | 
*V10Api* | [**v1_0_user_notifications_delete**](docs/V10Api.md#v1_0_user_notifications_delete) | **DELETE** /v1.0/user/notifications/{id}/ | 
*V10Api* | [**v1_0_user_notifications_list**](docs/V10Api.md#v1_0_user_notifications_list) | **GET** /v1.0/user/notifications/ | 
*V10Api* | [**v1_0_user_notifications_partial_update**](docs/V10Api.md#v1_0_user_notifications_partial_update) | **PATCH** /v1.0/user/notifications/{id}/ | 
*V10Api* | [**v1_0_user_notifications_read**](docs/V10Api.md#v1_0_user_notifications_read) | **GET** /v1.0/user/notifications/{id}/ | 
*V10Api* | [**v1_0_user_notifications_update**](docs/V10Api.md#v1_0_user_notifications_update) | **PUT** /v1.0/user/notifications/{id}/ | 
*V10Api* | [**v1_0_user_token_create**](docs/V10Api.md#v1_0_user_token_create) | **POST** /v1.0/user/token/ | 


## Documentation For Models

 - [AuthToken](docs/AuthToken.md)
 - [Channel](docs/Channel.md)
 - [Contact](docs/Contact.md)
 - [Dashboard](docs/Dashboard.md)
 - [Group](docs/Group.md)
 - [Metric](docs/Metric.md)
 - [NslcGroup](docs/NslcGroup.md)
 - [ReadOnlyAlertDetailSerializer](docs/ReadOnlyAlertDetailSerializer.md)
 - [ReadOnlyAlertSerializer](docs/ReadOnlyAlertSerializer.md)
 - [ReadOnlyArchiveDaySerializer](docs/ReadOnlyArchiveDaySerializer.md)
 - [ReadOnlyArchiveHourSerializer](docs/ReadOnlyArchiveHourSerializer.md)
 - [ReadOnlyArchiveMonthSerializer](docs/ReadOnlyArchiveMonthSerializer.md)
 - [ReadOnlyArchiveWeekSerializer](docs/ReadOnlyArchiveWeekSerializer.md)
 - [ReadOnlyChannelSerializer](docs/ReadOnlyChannelSerializer.md)
 - [ReadOnlyContactSerializer](docs/ReadOnlyContactSerializer.md)
 - [ReadOnlyDashboardDetailSerializer](docs/ReadOnlyDashboardDetailSerializer.md)
 - [ReadOnlyDashboardSerializer](docs/ReadOnlyDashboardSerializer.md)
 - [ReadOnlyEmailSerializer](docs/ReadOnlyEmailSerializer.md)
 - [ReadOnlyGroupDetailSerializer](docs/ReadOnlyGroupDetailSerializer.md)
 - [ReadOnlyGroupSerializer](docs/ReadOnlyGroupSerializer.md)
 - [ReadOnlyInviteRegisterSerializer](docs/ReadOnlyInviteRegisterSerializer.md)
 - [ReadOnlyInviteTokenSerializer](docs/ReadOnlyInviteTokenSerializer.md)
 - [ReadOnlyMeasurementSerializer](docs/ReadOnlyMeasurementSerializer.md)
 - [ReadOnlyMetricSerializer](docs/ReadOnlyMetricSerializer.md)
 - [ReadOnlyMonitorDetailSerializer](docs/ReadOnlyMonitorDetailSerializer.md)
 - [ReadOnlyMonitorSerializer](docs/ReadOnlyMonitorSerializer.md)
 - [ReadOnlyNetworkSerializer](docs/ReadOnlyNetworkSerializer.md)
 - [ReadOnlyNotificationDetailSerializer](docs/ReadOnlyNotificationDetailSerializer.md)
 - [ReadOnlyNotificationSerializer](docs/ReadOnlyNotificationSerializer.md)
 - [ReadOnlyOrganizationSerializer](docs/ReadOnlyOrganizationSerializer.md)
 - [ReadOnlyPasswordTokenSerializer](docs/ReadOnlyPasswordTokenSerializer.md)
 - [ReadOnlyStatTypeSerializer](docs/ReadOnlyStatTypeSerializer.md)
 - [ReadOnlyThresholdSerializer](docs/ReadOnlyThresholdSerializer.md)
 - [ReadOnlyTokenSerializer](docs/ReadOnlyTokenSerializer.md)
 - [ReadOnlyTriggerSerializer](docs/ReadOnlyTriggerSerializer.md)
 - [ReadOnlyUserGroupSerializer](docs/ReadOnlyUserGroupSerializer.md)
 - [ReadOnlyUserMeSerializer](docs/ReadOnlyUserMeSerializer.md)
 - [ReadOnlyUserReadSerializer](docs/ReadOnlyUserReadSerializer.md)
 - [ReadOnlyUserWriteSerializer](docs/ReadOnlyUserWriteSerializer.md)
 - [ReadOnlyWidgetDetailSerializer](docs/ReadOnlyWidgetDetailSerializer.md)
 - [ReadOnlyWidgetSerializer](docs/ReadOnlyWidgetSerializer.md)
 - [ReadOnlyWidgetTypeSerializer](docs/ReadOnlyWidgetTypeSerializer.md)
 - [StatType](docs/StatType.md)
 - [Threshold](docs/Threshold.md)
 - [Token](docs/Token.md)
 - [Trigger](docs/Trigger.md)
 - [UserSimple](docs/UserSimple.md)
 - [WidgetType](docs/WidgetType.md)
 - [WriteOnlyAlertSerializer](docs/WriteOnlyAlertSerializer.md)
 - [WriteOnlyChannelSerializer](docs/WriteOnlyChannelSerializer.md)
 - [WriteOnlyContactSerializer](docs/WriteOnlyContactSerializer.md)
 - [WriteOnlyDashboardSerializer](docs/WriteOnlyDashboardSerializer.md)
 - [WriteOnlyEmailSerializer](docs/WriteOnlyEmailSerializer.md)
 - [WriteOnlyGroupSerializer](docs/WriteOnlyGroupSerializer.md)
 - [WriteOnlyInviteRegisterSerializer](docs/WriteOnlyInviteRegisterSerializer.md)
 - [WriteOnlyInviteTokenSerializer](docs/WriteOnlyInviteTokenSerializer.md)
 - [WriteOnlyMeasurementSerializer](docs/WriteOnlyMeasurementSerializer.md)
 - [WriteOnlyMetricSerializer](docs/WriteOnlyMetricSerializer.md)
 - [WriteOnlyMonitorSerializer](docs/WriteOnlyMonitorSerializer.md)
 - [WriteOnlyNetworkSerializer](docs/WriteOnlyNetworkSerializer.md)
 - [WriteOnlyNotificationSerializer](docs/WriteOnlyNotificationSerializer.md)
 - [WriteOnlyOrganizationSerializer](docs/WriteOnlyOrganizationSerializer.md)
 - [WriteOnlyPasswordTokenSerializer](docs/WriteOnlyPasswordTokenSerializer.md)
 - [WriteOnlyStatTypeSerializer](docs/WriteOnlyStatTypeSerializer.md)
 - [WriteOnlyThresholdSerializer](docs/WriteOnlyThresholdSerializer.md)
 - [WriteOnlyTokenSerializer](docs/WriteOnlyTokenSerializer.md)
 - [WriteOnlyTriggerSerializer](docs/WriteOnlyTriggerSerializer.md)
 - [WriteOnlyUserGroupSerializer](docs/WriteOnlyUserGroupSerializer.md)
 - [WriteOnlyUserMeSerializer](docs/WriteOnlyUserMeSerializer.md)
 - [WriteOnlyUserWriteSerializer](docs/WriteOnlyUserWriteSerializer.md)
 - [WriteOnlyWidgetSerializer](docs/WriteOnlyWidgetSerializer.md)
 - [WriteOnlyWidgetTypeSerializer](docs/WriteOnlyWidgetTypeSerializer.md)


## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

contact@snippets.local

