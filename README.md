# squacapi_client
API for accessing squac data

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 2.1.11
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

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

All URIs are relative to *https://squacapi.pnsn.org/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**list**](docs/DefaultApi.md#list) | **GET** / | 
*ApiApi* | [**api_dashboard_dashboards_create**](docs/ApiApi.md#api_dashboard_dashboards_create) | **POST** /api/dashboard/dashboards/ | 
*ApiApi* | [**api_dashboard_dashboards_delete**](docs/ApiApi.md#api_dashboard_dashboards_delete) | **DELETE** /api/dashboard/dashboards/{id}/ | 
*ApiApi* | [**api_dashboard_dashboards_list**](docs/ApiApi.md#api_dashboard_dashboards_list) | **GET** /api/dashboard/dashboards/ | 
*ApiApi* | [**api_dashboard_dashboards_partial_update**](docs/ApiApi.md#api_dashboard_dashboards_partial_update) | **PATCH** /api/dashboard/dashboards/{id}/ | 
*ApiApi* | [**api_dashboard_dashboards_read**](docs/ApiApi.md#api_dashboard_dashboards_read) | **GET** /api/dashboard/dashboards/{id}/ | 
*ApiApi* | [**api_dashboard_dashboards_update**](docs/ApiApi.md#api_dashboard_dashboards_update) | **PUT** /api/dashboard/dashboards/{id}/ | 
*ApiApi* | [**api_dashboard_widgets_create**](docs/ApiApi.md#api_dashboard_widgets_create) | **POST** /api/dashboard/widgets/ | 
*ApiApi* | [**api_dashboard_widgets_delete**](docs/ApiApi.md#api_dashboard_widgets_delete) | **DELETE** /api/dashboard/widgets/{id}/ | 
*ApiApi* | [**api_dashboard_widgets_list**](docs/ApiApi.md#api_dashboard_widgets_list) | **GET** /api/dashboard/widgets/ | 
*ApiApi* | [**api_dashboard_widgets_partial_update**](docs/ApiApi.md#api_dashboard_widgets_partial_update) | **PATCH** /api/dashboard/widgets/{id}/ | 
*ApiApi* | [**api_dashboard_widgets_read**](docs/ApiApi.md#api_dashboard_widgets_read) | **GET** /api/dashboard/widgets/{id}/ | 
*ApiApi* | [**api_dashboard_widgets_update**](docs/ApiApi.md#api_dashboard_widgets_update) | **PUT** /api/dashboard/widgets/{id}/ | 
*ApiApi* | [**api_list**](docs/ApiApi.md#api_list) | **GET** /api/ | 
*ApiApi* | [**api_measurement_aggregated_list**](docs/ApiApi.md#api_measurement_aggregated_list) | **GET** /api/measurement/aggregated/ | 
*ApiApi* | [**api_measurement_alerts_create**](docs/ApiApi.md#api_measurement_alerts_create) | **POST** /api/measurement/alerts/ | 
*ApiApi* | [**api_measurement_alerts_delete**](docs/ApiApi.md#api_measurement_alerts_delete) | **DELETE** /api/measurement/alerts/{id}/ | 
*ApiApi* | [**api_measurement_alerts_list**](docs/ApiApi.md#api_measurement_alerts_list) | **GET** /api/measurement/alerts/ | 
*ApiApi* | [**api_measurement_alerts_partial_update**](docs/ApiApi.md#api_measurement_alerts_partial_update) | **PATCH** /api/measurement/alerts/{id}/ | 
*ApiApi* | [**api_measurement_alerts_read**](docs/ApiApi.md#api_measurement_alerts_read) | **GET** /api/measurement/alerts/{id}/ | 
*ApiApi* | [**api_measurement_alerts_update**](docs/ApiApi.md#api_measurement_alerts_update) | **PUT** /api/measurement/alerts/{id}/ | 
*ApiApi* | [**api_measurement_day_archives_list**](docs/ApiApi.md#api_measurement_day_archives_list) | **GET** /api/measurement/day-archives/ | 
*ApiApi* | [**api_measurement_day_archives_read**](docs/ApiApi.md#api_measurement_day_archives_read) | **GET** /api/measurement/day-archives/{id}/ | 
*ApiApi* | [**api_measurement_hour_archives_list**](docs/ApiApi.md#api_measurement_hour_archives_list) | **GET** /api/measurement/hour-archives/ | 
*ApiApi* | [**api_measurement_hour_archives_read**](docs/ApiApi.md#api_measurement_hour_archives_read) | **GET** /api/measurement/hour-archives/{id}/ | 
*ApiApi* | [**api_measurement_measurements_create**](docs/ApiApi.md#api_measurement_measurements_create) | **POST** /api/measurement/measurements/ | 
*ApiApi* | [**api_measurement_measurements_delete**](docs/ApiApi.md#api_measurement_measurements_delete) | **DELETE** /api/measurement/measurements/{id}/ | 
*ApiApi* | [**api_measurement_measurements_list**](docs/ApiApi.md#api_measurement_measurements_list) | **GET** /api/measurement/measurements/ | 
*ApiApi* | [**api_measurement_measurements_partial_update**](docs/ApiApi.md#api_measurement_measurements_partial_update) | **PATCH** /api/measurement/measurements/{id}/ | 
*ApiApi* | [**api_measurement_measurements_read**](docs/ApiApi.md#api_measurement_measurements_read) | **GET** /api/measurement/measurements/{id}/ | 
*ApiApi* | [**api_measurement_measurements_update**](docs/ApiApi.md#api_measurement_measurements_update) | **PUT** /api/measurement/measurements/{id}/ | 
*ApiApi* | [**api_measurement_metrics_create**](docs/ApiApi.md#api_measurement_metrics_create) | **POST** /api/measurement/metrics/ | 
*ApiApi* | [**api_measurement_metrics_delete**](docs/ApiApi.md#api_measurement_metrics_delete) | **DELETE** /api/measurement/metrics/{id}/ | 
*ApiApi* | [**api_measurement_metrics_list**](docs/ApiApi.md#api_measurement_metrics_list) | **GET** /api/measurement/metrics/ | 
*ApiApi* | [**api_measurement_metrics_partial_update**](docs/ApiApi.md#api_measurement_metrics_partial_update) | **PATCH** /api/measurement/metrics/{id}/ | 
*ApiApi* | [**api_measurement_metrics_read**](docs/ApiApi.md#api_measurement_metrics_read) | **GET** /api/measurement/metrics/{id}/ | 
*ApiApi* | [**api_measurement_metrics_update**](docs/ApiApi.md#api_measurement_metrics_update) | **PUT** /api/measurement/metrics/{id}/ | 
*ApiApi* | [**api_measurement_monitors_create**](docs/ApiApi.md#api_measurement_monitors_create) | **POST** /api/measurement/monitors/ | 
*ApiApi* | [**api_measurement_monitors_delete**](docs/ApiApi.md#api_measurement_monitors_delete) | **DELETE** /api/measurement/monitors/{id}/ | 
*ApiApi* | [**api_measurement_monitors_list**](docs/ApiApi.md#api_measurement_monitors_list) | **GET** /api/measurement/monitors/ | 
*ApiApi* | [**api_measurement_monitors_partial_update**](docs/ApiApi.md#api_measurement_monitors_partial_update) | **PATCH** /api/measurement/monitors/{id}/ | 
*ApiApi* | [**api_measurement_monitors_read**](docs/ApiApi.md#api_measurement_monitors_read) | **GET** /api/measurement/monitors/{id}/ | 
*ApiApi* | [**api_measurement_monitors_update**](docs/ApiApi.md#api_measurement_monitors_update) | **PUT** /api/measurement/monitors/{id}/ | 
*ApiApi* | [**api_measurement_month_archives_list**](docs/ApiApi.md#api_measurement_month_archives_list) | **GET** /api/measurement/month-archives/ | 
*ApiApi* | [**api_measurement_month_archives_read**](docs/ApiApi.md#api_measurement_month_archives_read) | **GET** /api/measurement/month-archives/{id}/ | 
*ApiApi* | [**api_measurement_triggers_create**](docs/ApiApi.md#api_measurement_triggers_create) | **POST** /api/measurement/triggers/ | 
*ApiApi* | [**api_measurement_triggers_delete**](docs/ApiApi.md#api_measurement_triggers_delete) | **DELETE** /api/measurement/triggers/{id}/ | 
*ApiApi* | [**api_measurement_triggers_list**](docs/ApiApi.md#api_measurement_triggers_list) | **GET** /api/measurement/triggers/ | 
*ApiApi* | [**api_measurement_triggers_partial_update**](docs/ApiApi.md#api_measurement_triggers_partial_update) | **PATCH** /api/measurement/triggers/{id}/ | 
*ApiApi* | [**api_measurement_triggers_read**](docs/ApiApi.md#api_measurement_triggers_read) | **GET** /api/measurement/triggers/{id}/ | 
*ApiApi* | [**api_measurement_triggers_update**](docs/ApiApi.md#api_measurement_triggers_update) | **PUT** /api/measurement/triggers/{id}/ | 
*ApiApi* | [**api_measurement_week_archives_list**](docs/ApiApi.md#api_measurement_week_archives_list) | **GET** /api/measurement/week-archives/ | 
*ApiApi* | [**api_measurement_week_archives_read**](docs/ApiApi.md#api_measurement_week_archives_read) | **GET** /api/measurement/week-archives/{id}/ | 
*ApiApi* | [**api_nslc_channels_create**](docs/ApiApi.md#api_nslc_channels_create) | **POST** /api/nslc/channels/ | 
*ApiApi* | [**api_nslc_channels_delete**](docs/ApiApi.md#api_nslc_channels_delete) | **DELETE** /api/nslc/channels/{id}/ | 
*ApiApi* | [**api_nslc_channels_list**](docs/ApiApi.md#api_nslc_channels_list) | **GET** /api/nslc/channels/ | 
*ApiApi* | [**api_nslc_channels_partial_update**](docs/ApiApi.md#api_nslc_channels_partial_update) | **PATCH** /api/nslc/channels/{id}/ | 
*ApiApi* | [**api_nslc_channels_read**](docs/ApiApi.md#api_nslc_channels_read) | **GET** /api/nslc/channels/{id}/ | 
*ApiApi* | [**api_nslc_channels_update**](docs/ApiApi.md#api_nslc_channels_update) | **PUT** /api/nslc/channels/{id}/ | 
*ApiApi* | [**api_nslc_groups_create**](docs/ApiApi.md#api_nslc_groups_create) | **POST** /api/nslc/groups/ | 
*ApiApi* | [**api_nslc_groups_delete**](docs/ApiApi.md#api_nslc_groups_delete) | **DELETE** /api/nslc/groups/{id}/ | 
*ApiApi* | [**api_nslc_groups_list**](docs/ApiApi.md#api_nslc_groups_list) | **GET** /api/nslc/groups/ | 
*ApiApi* | [**api_nslc_groups_partial_update**](docs/ApiApi.md#api_nslc_groups_partial_update) | **PATCH** /api/nslc/groups/{id}/ | 
*ApiApi* | [**api_nslc_groups_read**](docs/ApiApi.md#api_nslc_groups_read) | **GET** /api/nslc/groups/{id}/ | 
*ApiApi* | [**api_nslc_groups_update**](docs/ApiApi.md#api_nslc_groups_update) | **PUT** /api/nslc/groups/{id}/ | 
*ApiApi* | [**api_nslc_matching_rules_create**](docs/ApiApi.md#api_nslc_matching_rules_create) | **POST** /api/nslc/matching-rules/ | 
*ApiApi* | [**api_nslc_matching_rules_delete**](docs/ApiApi.md#api_nslc_matching_rules_delete) | **DELETE** /api/nslc/matching-rules/{id}/ | 
*ApiApi* | [**api_nslc_matching_rules_list**](docs/ApiApi.md#api_nslc_matching_rules_list) | **GET** /api/nslc/matching-rules/ | 
*ApiApi* | [**api_nslc_matching_rules_partial_update**](docs/ApiApi.md#api_nslc_matching_rules_partial_update) | **PATCH** /api/nslc/matching-rules/{id}/ | 
*ApiApi* | [**api_nslc_matching_rules_read**](docs/ApiApi.md#api_nslc_matching_rules_read) | **GET** /api/nslc/matching-rules/{id}/ | 
*ApiApi* | [**api_nslc_matching_rules_update**](docs/ApiApi.md#api_nslc_matching_rules_update) | **PUT** /api/nslc/matching-rules/{id}/ | 
*ApiApi* | [**api_nslc_networks_create**](docs/ApiApi.md#api_nslc_networks_create) | **POST** /api/nslc/networks/ | 
*ApiApi* | [**api_nslc_networks_delete**](docs/ApiApi.md#api_nslc_networks_delete) | **DELETE** /api/nslc/networks/{code}/ | 
*ApiApi* | [**api_nslc_networks_list**](docs/ApiApi.md#api_nslc_networks_list) | **GET** /api/nslc/networks/ | 
*ApiApi* | [**api_nslc_networks_partial_update**](docs/ApiApi.md#api_nslc_networks_partial_update) | **PATCH** /api/nslc/networks/{code}/ | 
*ApiApi* | [**api_nslc_networks_read**](docs/ApiApi.md#api_nslc_networks_read) | **GET** /api/nslc/networks/{code}/ | 
*ApiApi* | [**api_nslc_networks_update**](docs/ApiApi.md#api_nslc_networks_update) | **PUT** /api/nslc/networks/{code}/ | 
*ApiApi* | [**api_organization_organizations_create**](docs/ApiApi.md#api_organization_organizations_create) | **POST** /api/organization/organizations/ | 
*ApiApi* | [**api_organization_organizations_delete**](docs/ApiApi.md#api_organization_organizations_delete) | **DELETE** /api/organization/organizations/{id}/ | 
*ApiApi* | [**api_organization_organizations_list**](docs/ApiApi.md#api_organization_organizations_list) | **GET** /api/organization/organizations/ | 
*ApiApi* | [**api_organization_organizations_partial_update**](docs/ApiApi.md#api_organization_organizations_partial_update) | **PATCH** /api/organization/organizations/{id}/ | 
*ApiApi* | [**api_organization_organizations_read**](docs/ApiApi.md#api_organization_organizations_read) | **GET** /api/organization/organizations/{id}/ | 
*ApiApi* | [**api_organization_organizations_update**](docs/ApiApi.md#api_organization_organizations_update) | **PUT** /api/organization/organizations/{id}/ | 
*ApiApi* | [**api_organization_users_create**](docs/ApiApi.md#api_organization_users_create) | **POST** /api/organization/users/ | 
*ApiApi* | [**api_organization_users_delete**](docs/ApiApi.md#api_organization_users_delete) | **DELETE** /api/organization/users/{id}/ | 
*ApiApi* | [**api_organization_users_list**](docs/ApiApi.md#api_organization_users_list) | **GET** /api/organization/users/ | 
*ApiApi* | [**api_organization_users_partial_update**](docs/ApiApi.md#api_organization_users_partial_update) | **PATCH** /api/organization/users/{id}/ | 
*ApiApi* | [**api_organization_users_read**](docs/ApiApi.md#api_organization_users_read) | **GET** /api/organization/users/{id}/ | 
*ApiApi* | [**api_organization_users_update**](docs/ApiApi.md#api_organization_users_update) | **PUT** /api/organization/users/{id}/ | 
*ApiApi* | [**api_password_reset_confirm_create**](docs/ApiApi.md#api_password_reset_confirm_create) | **POST** /api/password_reset/confirm/ | 
*ApiApi* | [**api_password_reset_create**](docs/ApiApi.md#api_password_reset_create) | **POST** /api/password_reset/ | An Api View which provides a method to request a password reset token based on an e-mail address
*ApiApi* | [**api_password_reset_validate_token_create**](docs/ApiApi.md#api_password_reset_validate_token_create) | **POST** /api/password_reset/validate_token/ | 
*ApiApi* | [**api_user_create_create**](docs/ApiApi.md#api_user_create_create) | **POST** /api/user/create/ | 
*ApiApi* | [**api_user_groups_create**](docs/ApiApi.md#api_user_groups_create) | **POST** /api/user/groups/ | 
*ApiApi* | [**api_user_groups_delete**](docs/ApiApi.md#api_user_groups_delete) | **DELETE** /api/user/groups/{id}/ | 
*ApiApi* | [**api_user_groups_list**](docs/ApiApi.md#api_user_groups_list) | **GET** /api/user/groups/ | 
*ApiApi* | [**api_user_groups_partial_update**](docs/ApiApi.md#api_user_groups_partial_update) | **PATCH** /api/user/groups/{id}/ | 
*ApiApi* | [**api_user_groups_read**](docs/ApiApi.md#api_user_groups_read) | **GET** /api/user/groups/{id}/ | 
*ApiApi* | [**api_user_groups_update**](docs/ApiApi.md#api_user_groups_update) | **PUT** /api/user/groups/{id}/ | 
*ApiApi* | [**api_user_me_partial_update**](docs/ApiApi.md#api_user_me_partial_update) | **PATCH** /api/user/me/ | 
*ApiApi* | [**api_user_me_read**](docs/ApiApi.md#api_user_me_read) | **GET** /api/user/me/ | 
*ApiApi* | [**api_user_token_create**](docs/ApiApi.md#api_user_token_create) | **POST** /api/user/token/ | 
*InviteApi* | [**invite_invite_create**](docs/InviteApi.md#invite_invite_create) | **POST** /invite/invite/ | 
*InviteApi* | [**invite_register_create**](docs/InviteApi.md#invite_register_create) | **POST** /invite/register/ | 

## Documentation For Models

 - [AuthToken](docs/AuthToken.md)
 - [Channel](docs/Channel.md)
 - [Measurement](docs/Measurement.md)
 - [Metric](docs/Metric.md)
 - [NslcGroup](docs/NslcGroup.md)
 - [ReadOnlyAlertDetailSerializer](docs/ReadOnlyAlertDetailSerializer.md)
 - [ReadOnlyAlertSerializer](docs/ReadOnlyAlertSerializer.md)
 - [ReadOnlyArchiveDaySerializer](docs/ReadOnlyArchiveDaySerializer.md)
 - [ReadOnlyArchiveHourSerializer](docs/ReadOnlyArchiveHourSerializer.md)
 - [ReadOnlyArchiveMonthSerializer](docs/ReadOnlyArchiveMonthSerializer.md)
 - [ReadOnlyArchiveWeekSerializer](docs/ReadOnlyArchiveWeekSerializer.md)
 - [ReadOnlyChannelSerializer](docs/ReadOnlyChannelSerializer.md)
 - [ReadOnlyDashboardDetailSerializer](docs/ReadOnlyDashboardDetailSerializer.md)
 - [ReadOnlyDashboardSerializer](docs/ReadOnlyDashboardSerializer.md)
 - [ReadOnlyEmailSerializer](docs/ReadOnlyEmailSerializer.md)
 - [ReadOnlyGroupDetailSerializer](docs/ReadOnlyGroupDetailSerializer.md)
 - [ReadOnlyGroupSerializer](docs/ReadOnlyGroupSerializer.md)
 - [ReadOnlyInviteRegisterSerializer](docs/ReadOnlyInviteRegisterSerializer.md)
 - [ReadOnlyInviteTokenSerializer](docs/ReadOnlyInviteTokenSerializer.md)
 - [ReadOnlyMatchingRuleSerializer](docs/ReadOnlyMatchingRuleSerializer.md)
 - [ReadOnlyMeasurementSerializer](docs/ReadOnlyMeasurementSerializer.md)
 - [ReadOnlyMetricSerializer](docs/ReadOnlyMetricSerializer.md)
 - [ReadOnlyMonitorDetailSerializer](docs/ReadOnlyMonitorDetailSerializer.md)
 - [ReadOnlyMonitorSerializer](docs/ReadOnlyMonitorSerializer.md)
 - [ReadOnlyNetworkSerializer](docs/ReadOnlyNetworkSerializer.md)
 - [ReadOnlyOrganizationSerializer](docs/ReadOnlyOrganizationSerializer.md)
 - [ReadOnlyPasswordTokenSerializer](docs/ReadOnlyPasswordTokenSerializer.md)
 - [ReadOnlyTokenSerializer](docs/ReadOnlyTokenSerializer.md)
 - [ReadOnlyTriggerSerializer](docs/ReadOnlyTriggerSerializer.md)
 - [ReadOnlyUserGroupSerializer](docs/ReadOnlyUserGroupSerializer.md)
 - [ReadOnlyUserMeSerializer](docs/ReadOnlyUserMeSerializer.md)
 - [ReadOnlyUserSerializer](docs/ReadOnlyUserSerializer.md)
 - [ReadOnlyUserSimpleSerializer](docs/ReadOnlyUserSimpleSerializer.md)
 - [ReadOnlyUserUpdateSerializer](docs/ReadOnlyUserUpdateSerializer.md)
 - [ReadOnlyWidgetDetailSerializer](docs/ReadOnlyWidgetDetailSerializer.md)
 - [ReadOnlyWidgetSerializer](docs/ReadOnlyWidgetSerializer.md)
 - [Token](docs/Token.md)
 - [Trigger](docs/Trigger.md)
 - [UserGroup](docs/UserGroup.md)
 - [UserSimple](docs/UserSimple.md)
 - [WriteOnlyAlertSerializer](docs/WriteOnlyAlertSerializer.md)
 - [WriteOnlyChannelSerializer](docs/WriteOnlyChannelSerializer.md)
 - [WriteOnlyDashboardSerializer](docs/WriteOnlyDashboardSerializer.md)
 - [WriteOnlyEmailSerializer](docs/WriteOnlyEmailSerializer.md)
 - [WriteOnlyGroupSerializer](docs/WriteOnlyGroupSerializer.md)
 - [WriteOnlyInviteRegisterSerializer](docs/WriteOnlyInviteRegisterSerializer.md)
 - [WriteOnlyInviteTokenSerializer](docs/WriteOnlyInviteTokenSerializer.md)
 - [WriteOnlyMatchingRuleSerializer](docs/WriteOnlyMatchingRuleSerializer.md)
 - [WriteOnlyMeasurementSerializer](docs/WriteOnlyMeasurementSerializer.md)
 - [WriteOnlyMetricSerializer](docs/WriteOnlyMetricSerializer.md)
 - [WriteOnlyMonitorSerializer](docs/WriteOnlyMonitorSerializer.md)
 - [WriteOnlyNetworkSerializer](docs/WriteOnlyNetworkSerializer.md)
 - [WriteOnlyOrganizationSerializer](docs/WriteOnlyOrganizationSerializer.md)
 - [WriteOnlyPasswordTokenSerializer](docs/WriteOnlyPasswordTokenSerializer.md)
 - [WriteOnlyTokenSerializer](docs/WriteOnlyTokenSerializer.md)
 - [WriteOnlyTriggerSerializer](docs/WriteOnlyTriggerSerializer.md)
 - [WriteOnlyUserGroupSerializer](docs/WriteOnlyUserGroupSerializer.md)
 - [WriteOnlyUserMeSerializer](docs/WriteOnlyUserMeSerializer.md)
 - [WriteOnlyUserSerializer](docs/WriteOnlyUserSerializer.md)
 - [WriteOnlyUserUpdateSerializer](docs/WriteOnlyUserUpdateSerializer.md)
 - [WriteOnlyWidgetSerializer](docs/WriteOnlyWidgetSerializer.md)

## Documentation For Authorization


## Token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

contact@snippets.local
