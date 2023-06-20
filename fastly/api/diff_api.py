"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://developer.fastly.com/reference/api/)   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: oss@fastly.com
"""


import re  # noqa: F401
import sys  # noqa: F401

from fastly.api_client import ApiClient, Endpoint as _Endpoint
from fastly.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fastly.model.diff_response import DiffResponse


class DiffApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.diff_service_versions_endpoint = _Endpoint(
            settings={
                'response_type': (DiffResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/diff/from/{from_version_id}/to/{to_version_id}',
                'operation_id': 'diff_service_versions',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'from_version_id',
                    'to_version_id',
                    'format',
                ],
                'required': [
                    'service_id',
                    'from_version_id',
                    'to_version_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'format',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('format',): {

                        "TEXT": "text",
                        "HTML": "html",
                        "HTML_SIMPLE": "html_simple"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'from_version_id':
                        (int,),
                    'to_version_id':
                        (int,),
                    'format':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'from_version_id': 'from_version_id',
                    'to_version_id': 'to_version_id',
                    'format': 'format',
                },
                'location_map': {
                    'service_id': 'path',
                    'from_version_id': 'path',
                    'to_version_id': 'path',
                    'format': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def diff_service_versions(
        self,
        service_id,
        from_version_id,
        to_version_id,
        **kwargs
    ):
        """Diff two service versions  # noqa: E501

        Get diff between two versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.diff_service_versions(service_id, from_version_id, to_version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            from_version_id (int): The version number of the service to which changes in the generated VCL are being compared. Can either be a positive number from 1 to your maximum version or a negative number from -1 down (-1 is latest version etc).
            to_version_id (int): The version number of the service from which changes in the generated VCL are being compared. Uses same numbering scheme as `from`.

        Keyword Args:
            format (str): Optional method to format the diff field.. [optional] if omitted the server will use the default value of "text"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            DiffResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['from_version_id'] = \
            from_version_id
        kwargs['to_version_id'] = \
            to_version_id
        return self.diff_service_versions_endpoint.call_with_http_info(**kwargs)

