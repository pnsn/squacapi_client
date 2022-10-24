# coding: utf-8

"""
    Squac API

    API for accessing squac data  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from squacapi_client.api_client import ApiClient


class InviteApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def invite_invite_create(self, body, **kwargs):  # noqa: E501
        """invite_invite_create  # noqa: E501

        Endpoint to invite an inactive user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_invite_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WriteOnlyInviteTokenSerializer body: (required)
        :return: ReadOnlyInviteTokenSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.invite_invite_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.invite_invite_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def invite_invite_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """invite_invite_create  # noqa: E501

        Endpoint to invite an inactive user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_invite_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WriteOnlyInviteTokenSerializer body: (required)
        :return: ReadOnlyInviteTokenSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invite_invite_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `invite_invite_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/invite/invite/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReadOnlyInviteTokenSerializer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invite_register_create(self, body, **kwargs):  # noqa: E501
        """invite_register_create  # noqa: E501

        called when invited user authenticates with token and sets password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_register_create(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WriteOnlyInviteRegisterSerializer body: (required)
        :return: ReadOnlyInviteRegisterSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.invite_register_create_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.invite_register_create_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def invite_register_create_with_http_info(self, body, **kwargs):  # noqa: E501
        """invite_register_create  # noqa: E501

        called when invited user authenticates with token and sets password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.invite_register_create_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WriteOnlyInviteRegisterSerializer body: (required)
        :return: ReadOnlyInviteRegisterSerializer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invite_register_create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `invite_register_create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/invite/register/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReadOnlyInviteRegisterSerializer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)