'''utility functions for uploading bulk measurments'''

from squacapi_client.rest import ApiException
from squacapi_client import Configuration, ApiClient, \
    UserApi, AuthToken, V10Api

# always default to a staging/test env



def get_client(user, passwd, host):
    '''authenticate user'''
    conf = Configuration()
    api_client = ApiClient(conf)
    # set host here
    api_client.configuration.host = host
    print(api_client.configuration.host)
    user_client = UserApi(ApiClient())
    auth_token = AuthToken(email=user, password=passwd)
    token = user_client.user_token_create(auth_token)
    conf.api_key['Authorization'] = token.token
    conf.api_key_prefix['Authorization'] = 'Token'
    return V10Api(api_client)


def make_channel_map(channels):
    '''create a dict where key = scnl and val is db id'''
    channel_map = {}
    for channel in channels:
        chan_key = channel.station_code.upper() + "." + channel.code.upper() + "." + channel.network.upper() + "." + channel.loc
        channel_map[chan_key] = channel.id
    return channel_map


def make_metric_map(metrics):
    '''create a dict where key = metric name and val is db id'''
    metric_map = {}
    for metric in metrics:
        metric_map[metric.name] = metric.id
    return metric_map


def perform_bulk_create(measurements, client, *args, **kwargs):

    '''post in chunks
        
        ensures atomicty. All in chunk write or none

        params:
            measurements: list of WriteOnlyMeasurementSerializer
            client: Api client
            *args
            *kwargs
                chunk size of list to post
        returns
            resp: list of ReadOnlyMeasurementSerialer objects
            errors tuple (response, error)
    '''
    response = []
    errors = []
    start = 0
    if 'chunk' in kwargs:
        chunk = kwargs['chunk']
    else:
        chunk = 100
    end = chunk
    while start < len(measurements):
        print("start:{} stop:{} ".format(start, end))
        collection = measurements[start:end]
        try:
            resp = client.v1_0_measurement_measurements_create(collection)
        except ApiException as e:
            errors.append(resp, e)
        start += chunk
        end += chunk
        response += resp
    return response, errors
