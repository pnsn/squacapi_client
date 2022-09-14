# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from squacapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from squacapi_client.model.auth_token import AuthToken
from squacapi_client.model.channel import Channel
from squacapi_client.model.group import Group
from squacapi_client.model.measurement import Measurement
from squacapi_client.model.metric import Metric
from squacapi_client.model.nslc_group import NslcGroup
from squacapi_client.model.read_only_alert_detail_serializer import ReadOnlyAlertDetailSerializer
from squacapi_client.model.read_only_alert_serializer import ReadOnlyAlertSerializer
from squacapi_client.model.read_only_archive_day_serializer import ReadOnlyArchiveDaySerializer
from squacapi_client.model.read_only_archive_hour_serializer import ReadOnlyArchiveHourSerializer
from squacapi_client.model.read_only_archive_month_serializer import ReadOnlyArchiveMonthSerializer
from squacapi_client.model.read_only_archive_week_serializer import ReadOnlyArchiveWeekSerializer
from squacapi_client.model.read_only_channel_serializer import ReadOnlyChannelSerializer
from squacapi_client.model.read_only_dashboard_detail_serializer import ReadOnlyDashboardDetailSerializer
from squacapi_client.model.read_only_dashboard_serializer import ReadOnlyDashboardSerializer
from squacapi_client.model.read_only_email_serializer import ReadOnlyEmailSerializer
from squacapi_client.model.read_only_group_detail_serializer import ReadOnlyGroupDetailSerializer
from squacapi_client.model.read_only_group_serializer import ReadOnlyGroupSerializer
from squacapi_client.model.read_only_matching_rule_serializer import ReadOnlyMatchingRuleSerializer
from squacapi_client.model.read_only_measurement_serializer import ReadOnlyMeasurementSerializer
from squacapi_client.model.read_only_metric_serializer import ReadOnlyMetricSerializer
from squacapi_client.model.read_only_monitor_detail_serializer import ReadOnlyMonitorDetailSerializer
from squacapi_client.model.read_only_monitor_serializer import ReadOnlyMonitorSerializer
from squacapi_client.model.read_only_network_serializer import ReadOnlyNetworkSerializer
from squacapi_client.model.read_only_organization_serializer import ReadOnlyOrganizationSerializer
from squacapi_client.model.read_only_password_token_serializer import ReadOnlyPasswordTokenSerializer
from squacapi_client.model.read_only_token_serializer import ReadOnlyTokenSerializer
from squacapi_client.model.read_only_trigger_serializer import ReadOnlyTriggerSerializer
from squacapi_client.model.read_only_user_me_serializer import ReadOnlyUserMeSerializer
from squacapi_client.model.read_only_user_read_serializer import ReadOnlyUserReadSerializer
from squacapi_client.model.read_only_user_write_serializer import ReadOnlyUserWriteSerializer
from squacapi_client.model.read_only_widget_detail_serializer import ReadOnlyWidgetDetailSerializer
from squacapi_client.model.read_only_widget_serializer import ReadOnlyWidgetSerializer
from squacapi_client.model.token import Token
from squacapi_client.model.trigger import Trigger
from squacapi_client.model.user_groups_list200_response import UserGroupsList200Response
from squacapi_client.model.user_simple import UserSimple
from squacapi_client.model.v10_dashboard_dashboards_list200_response import V10DashboardDashboardsList200Response
from squacapi_client.model.v10_dashboard_widgets_list200_response import V10DashboardWidgetsList200Response
from squacapi_client.model.v10_measurement_alerts_list200_response import V10MeasurementAlertsList200Response
from squacapi_client.model.v10_measurement_day_archives_list200_response import V10MeasurementDayArchivesList200Response
from squacapi_client.model.v10_measurement_hour_archives_list200_response import V10MeasurementHourArchivesList200Response
from squacapi_client.model.v10_measurement_measurements_list200_response import V10MeasurementMeasurementsList200Response
from squacapi_client.model.v10_measurement_metrics_list200_response import V10MeasurementMetricsList200Response
from squacapi_client.model.v10_measurement_monitors_list200_response import V10MeasurementMonitorsList200Response
from squacapi_client.model.v10_measurement_month_archives_list200_response import V10MeasurementMonthArchivesList200Response
from squacapi_client.model.v10_measurement_triggers_list200_response import V10MeasurementTriggersList200Response
from squacapi_client.model.v10_measurement_week_archives_list200_response import V10MeasurementWeekArchivesList200Response
from squacapi_client.model.v10_nslc_channels_list200_response import V10NslcChannelsList200Response
from squacapi_client.model.v10_nslc_groups_list200_response import V10NslcGroupsList200Response
from squacapi_client.model.v10_nslc_matching_rules_list200_response import V10NslcMatchingRulesList200Response
from squacapi_client.model.v10_nslc_networks_list200_response import V10NslcNetworksList200Response
from squacapi_client.model.v10_organization_organizations_list200_response import V10OrganizationOrganizationsList200Response
from squacapi_client.model.v10_organization_users_list200_response import V10OrganizationUsersList200Response
from squacapi_client.model.write_only_alert_serializer import WriteOnlyAlertSerializer
from squacapi_client.model.write_only_channel_serializer import WriteOnlyChannelSerializer
from squacapi_client.model.write_only_dashboard_serializer import WriteOnlyDashboardSerializer
from squacapi_client.model.write_only_email_serializer import WriteOnlyEmailSerializer
from squacapi_client.model.write_only_group_serializer import WriteOnlyGroupSerializer
from squacapi_client.model.write_only_matching_rule_serializer import WriteOnlyMatchingRuleSerializer
from squacapi_client.model.write_only_measurement_serializer import WriteOnlyMeasurementSerializer
from squacapi_client.model.write_only_metric_serializer import WriteOnlyMetricSerializer
from squacapi_client.model.write_only_monitor_serializer import WriteOnlyMonitorSerializer
from squacapi_client.model.write_only_network_serializer import WriteOnlyNetworkSerializer
from squacapi_client.model.write_only_organization_serializer import WriteOnlyOrganizationSerializer
from squacapi_client.model.write_only_password_token_serializer import WriteOnlyPasswordTokenSerializer
from squacapi_client.model.write_only_token_serializer import WriteOnlyTokenSerializer
from squacapi_client.model.write_only_trigger_serializer import WriteOnlyTriggerSerializer
from squacapi_client.model.write_only_user_me_serializer import WriteOnlyUserMeSerializer
from squacapi_client.model.write_only_user_write_serializer import WriteOnlyUserWriteSerializer
from squacapi_client.model.write_only_widget_serializer import WriteOnlyWidgetSerializer
