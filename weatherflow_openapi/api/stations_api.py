# coding: utf-8

"""
    WeatherFlow Tempest API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: jforare@weatherflow.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing import overload, Optional, Union, Awaitable

from typing_extensions import Annotated
from pydantic import Field, StrictInt

from weatherflow_openapi.models.station_set import StationSet

from weatherflow_openapi.api_client import ApiClient
from weatherflow_openapi.api_response import ApiResponse
from weatherflow_openapi.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class StationsApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @overload
    async def get_station_by_id(self, station_id : Annotated[StrictInt, Field(..., description="ID of Station to return")], **kwargs) -> StationSet:  # noqa: E501
        ...

    @overload
    def get_station_by_id(self, station_id : Annotated[StrictInt, Field(..., description="ID of Station to return")], async_req: Optional[bool]=True, **kwargs) -> StationSet:  # noqa: E501
        ...

    @validate_arguments
    def get_station_by_id(self, station_id : Annotated[StrictInt, Field(..., description="ID of Station to return")], async_req: Optional[bool]=None, **kwargs) -> Union[StationSet, Awaitable[StationSet]]:  # noqa: E501
        """Find a Station by station_id  # noqa: E501

        Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_station_by_id(station_id, async_req=True)
        >>> result = thread.get()

        :param station_id: ID of Station to return (required)
        :type station_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StationSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_station_by_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_station_by_id_with_http_info(station_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_station_by_id_with_http_info(self, station_id : Annotated[StrictInt, Field(..., description="ID of Station to return")], **kwargs) -> ApiResponse:  # noqa: E501
        """Find a Station by station_id  # noqa: E501

        Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_station_by_id_with_http_info(station_id, async_req=True)
        >>> result = thread.get()

        :param station_id: ID of Station to return (required)
        :type station_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StationSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'station_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_station_by_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['station_id']:
            _path_params['station_id'] = _params['station_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['swdApiKey', 'swdImplicit']  # noqa: E501

        _response_types_map = {
            '200': "StationSet",
            '404': None,
        }

        return self.api_client.call_api(
            '/stations/{station_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @overload
    async def get_stations(self, **kwargs) -> StationSet:  # noqa: E501
        ...

    @overload
    def get_stations(self, async_req: Optional[bool]=True, **kwargs) -> StationSet:  # noqa: E501
        ...

    @validate_arguments
    def get_stations(self, async_req: Optional[bool]=None, **kwargs) -> Union[StationSet, Awaitable[StationSet]]:  # noqa: E501
        """Find all Stations for a user  # noqa: E501

        Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_stations(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request.
               If one number provided, it will be total request
               timeout. It can also be a pair (tuple) of
               (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StationSet
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            message = "Error! Please call the get_stations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data"  # noqa: E501
            raise ValueError(message)
        if async_req is not None:
            kwargs['async_req'] = async_req
        return self.get_stations_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_stations_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Find all Stations for a user  # noqa: E501

        Devices all belong to a Station.  This response contains Station metadata and metadata for the Devices in it.  Each user can create multiple Stations.  A Device can only be in one Station at a time.  Only devices with a serial_number value can send new observations.  A Device wihout a serial_number indicates that Device is no longer active.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_stations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(StationSet, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_stations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['swdApiKey', 'swdImplicit']  # noqa: E501

        _response_types_map = {
            '200': "StationSet",
            '404': None,
        }

        return self.api_client.call_api(
            '/stations', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
