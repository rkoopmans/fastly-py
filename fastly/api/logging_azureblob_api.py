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
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.logging_azureblob_response import LoggingAzureblobResponse


class LoggingAzureblobApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_log_azure_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingAzureblobResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/azureblob',
                'operation_id': 'create_log_azure',
                'http_method': 'POST',
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
                    'version_id',
                    'name',
                    'placement',
                    'response_condition',
                    'format',
                    'format_version',
                    'message_type',
                    'timestamp_format',
                    'compression_codec',
                    'period',
                    'gzip_level',
                    'path',
                    'account_name',
                    'container',
                    'sas_token',
                    'public_key',
                    'file_max_bytes',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'timestamp_format',
                    'path',
                    'public_key',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'message_type',
                    'compression_codec',
                ],
                'validation': [
                    'file_max_bytes',
                ]
            },
            root_map={
                'validations': {
                    ('file_max_bytes',): {

                        'inclusive_minimum': 1048576,
                    },
                },
                'allowed_values': {
                    ('placement',): {
                        'None': None,
                        "NONE": "none",
                        "WAF_DEBUG": "waf_debug",
                        "NULL": "null"
                    },
                    ('format_version',): {

                        "v1": 1,
                        "v2": 2
                    },
                    ('message_type',): {

                        "CLASSIC": "classic",
                        "LOGGLY": "loggly",
                        "LOGPLEX": "logplex",
                        "BLANK": "blank"
                    },
                    ('compression_codec',): {

                        "ZSTD": "zstd",
                        "SNAPPY": "snappy",
                        "GZIP": "gzip"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'name':
                        (str,),
                    'placement':
                        (str, none_type,),
                    'response_condition':
                        (str, none_type,),
                    'format':
                        (str,),
                    'format_version':
                        (int,),
                    'message_type':
                        (str,),
                    'timestamp_format':
                        (str, none_type,),
                    'compression_codec':
                        (str,),
                    'period':
                        (int,),
                    'gzip_level':
                        (int,),
                    'path':
                        (str, none_type,),
                    'account_name':
                        (str,),
                    'container':
                        (str,),
                    'sas_token':
                        (str,),
                    'public_key':
                        (str, none_type,),
                    'file_max_bytes':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'name': 'name',
                    'placement': 'placement',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'format_version': 'format_version',
                    'message_type': 'message_type',
                    'timestamp_format': 'timestamp_format',
                    'compression_codec': 'compression_codec',
                    'period': 'period',
                    'gzip_level': 'gzip_level',
                    'path': 'path',
                    'account_name': 'account_name',
                    'container': 'container',
                    'sas_token': 'sas_token',
                    'public_key': 'public_key',
                    'file_max_bytes': 'file_max_bytes',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'format_version': 'form',
                    'message_type': 'form',
                    'timestamp_format': 'form',
                    'compression_codec': 'form',
                    'period': 'form',
                    'gzip_level': 'form',
                    'path': 'form',
                    'account_name': 'form',
                    'container': 'form',
                    'sas_token': 'form',
                    'public_key': 'form',
                    'file_max_bytes': 'form',
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
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.delete_log_azure_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name}',
                'operation_id': 'delete_log_azure',
                'http_method': 'DELETE',
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
                    'version_id',
                    'logging_azureblob_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_azureblob_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_azureblob_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_azureblob_name': 'logging_azureblob_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_azureblob_name': 'path',
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
        self.get_log_azure_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingAzureblobResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name}',
                'operation_id': 'get_log_azure',
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
                    'version_id',
                    'logging_azureblob_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_azureblob_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_azureblob_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_azureblob_name': 'logging_azureblob_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_azureblob_name': 'path',
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
        self.list_log_azure_endpoint = _Endpoint(
            settings={
                'response_type': ([LoggingAzureblobResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/azureblob',
                'operation_id': 'list_log_azure',
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
                    'version_id',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
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
        self.update_log_azure_endpoint = _Endpoint(
            settings={
                'response_type': (LoggingAzureblobResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name}',
                'operation_id': 'update_log_azure',
                'http_method': 'PUT',
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
                    'version_id',
                    'logging_azureblob_name',
                    'name',
                    'placement',
                    'response_condition',
                    'format',
                    'format_version',
                    'message_type',
                    'timestamp_format',
                    'compression_codec',
                    'period',
                    'gzip_level',
                    'path',
                    'account_name',
                    'container',
                    'sas_token',
                    'public_key',
                    'file_max_bytes',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'logging_azureblob_name',
                ],
                'nullable': [
                    'placement',
                    'response_condition',
                    'timestamp_format',
                    'path',
                    'public_key',
                ],
                'enum': [
                    'placement',
                    'format_version',
                    'message_type',
                    'compression_codec',
                ],
                'validation': [
                    'file_max_bytes',
                ]
            },
            root_map={
                'validations': {
                    ('file_max_bytes',): {

                        'inclusive_minimum': 1048576,
                    },
                },
                'allowed_values': {
                    ('placement',): {
                        'None': None,
                        "NONE": "none",
                        "WAF_DEBUG": "waf_debug",
                        "NULL": "null"
                    },
                    ('format_version',): {

                        "v1": 1,
                        "v2": 2
                    },
                    ('message_type',): {

                        "CLASSIC": "classic",
                        "LOGGLY": "loggly",
                        "LOGPLEX": "logplex",
                        "BLANK": "blank"
                    },
                    ('compression_codec',): {

                        "ZSTD": "zstd",
                        "SNAPPY": "snappy",
                        "GZIP": "gzip"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'logging_azureblob_name':
                        (str,),
                    'name':
                        (str,),
                    'placement':
                        (str, none_type,),
                    'response_condition':
                        (str, none_type,),
                    'format':
                        (str,),
                    'format_version':
                        (int,),
                    'message_type':
                        (str,),
                    'timestamp_format':
                        (str, none_type,),
                    'compression_codec':
                        (str,),
                    'period':
                        (int,),
                    'gzip_level':
                        (int,),
                    'path':
                        (str, none_type,),
                    'account_name':
                        (str,),
                    'container':
                        (str,),
                    'sas_token':
                        (str,),
                    'public_key':
                        (str, none_type,),
                    'file_max_bytes':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'logging_azureblob_name': 'logging_azureblob_name',
                    'name': 'name',
                    'placement': 'placement',
                    'response_condition': 'response_condition',
                    'format': 'format',
                    'format_version': 'format_version',
                    'message_type': 'message_type',
                    'timestamp_format': 'timestamp_format',
                    'compression_codec': 'compression_codec',
                    'period': 'period',
                    'gzip_level': 'gzip_level',
                    'path': 'path',
                    'account_name': 'account_name',
                    'container': 'container',
                    'sas_token': 'sas_token',
                    'public_key': 'public_key',
                    'file_max_bytes': 'file_max_bytes',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'logging_azureblob_name': 'path',
                    'name': 'form',
                    'placement': 'form',
                    'response_condition': 'form',
                    'format': 'form',
                    'format_version': 'form',
                    'message_type': 'form',
                    'timestamp_format': 'form',
                    'compression_codec': 'form',
                    'period': 'form',
                    'gzip_level': 'form',
                    'path': 'form',
                    'account_name': 'form',
                    'container': 'form',
                    'sas_token': 'form',
                    'public_key': 'form',
                    'file_max_bytes': 'form',
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
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def create_log_azure(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create an Azure Blob Storage log endpoint  # noqa: E501

        Create an Azure Blob Storage logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_log_azure(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            message_type (str): How the message should be formatted.. [optional] if omitted the server will use the default value of "classic"
            timestamp_format (str, none_type): A timestamp format. [optional]
            compression_codec (str): The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional]
            period (int): How frequently log files are finalized so they can be available for reading (in seconds).. [optional] if omitted the server will use the default value of 3600
            gzip_level (int): The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional] if omitted the server will use the default value of 0
            path (str, none_type): The path to upload logs to.. [optional] if omitted the server will use the default value of "null"
            account_name (str): The unique Azure Blob Storage namespace in which your data objects are stored. Required.. [optional]
            container (str): The name of the Azure Blob Storage container in which to store logs. Required.. [optional]
            sas_token (str): The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required.. [optional]
            public_key (str, none_type): A PGP public key that Fastly will use to encrypt your log files before writing them to disk.. [optional] if omitted the server will use the default value of "null"
            file_max_bytes (int): The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.). [optional]
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
            LoggingAzureblobResponse
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
        kwargs['version_id'] = \
            version_id
        return self.create_log_azure_endpoint.call_with_http_info(**kwargs)

    def delete_log_azure(
        self,
        service_id,
        version_id,
        logging_azureblob_name,
        **kwargs
    ):
        """Delete the Azure Blob Storage log endpoint  # noqa: E501

        Delete the Azure Blob Storage logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_log_azure(service_id, version_id, logging_azureblob_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_azureblob_name (str): The name for the real-time logging configuration.

        Keyword Args:
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
            InlineResponse200
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
        kwargs['version_id'] = \
            version_id
        kwargs['logging_azureblob_name'] = \
            logging_azureblob_name
        return self.delete_log_azure_endpoint.call_with_http_info(**kwargs)

    def get_log_azure(
        self,
        service_id,
        version_id,
        logging_azureblob_name,
        **kwargs
    ):
        """Get an Azure Blob Storage log endpoint  # noqa: E501

        Get the Azure Blob Storage logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_log_azure(service_id, version_id, logging_azureblob_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_azureblob_name (str): The name for the real-time logging configuration.

        Keyword Args:
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
            LoggingAzureblobResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['logging_azureblob_name'] = \
            logging_azureblob_name
        return self.get_log_azure_endpoint.call_with_http_info(**kwargs)

    def list_log_azure(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List Azure Blob Storage log endpoints  # noqa: E501

        List all of the Azure Blob Storage logging endpoints for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_log_azure(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
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
            [LoggingAzureblobResponse]
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
        kwargs['version_id'] = \
            version_id
        return self.list_log_azure_endpoint.call_with_http_info(**kwargs)

    def update_log_azure(
        self,
        service_id,
        version_id,
        logging_azureblob_name,
        **kwargs
    ):
        """Update an Azure Blob Storage log endpoint  # noqa: E501

        Update the Azure Blob Storage logging endpoint for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_log_azure(service_id, version_id, logging_azureblob_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            logging_azureblob_name (str): The name for the real-time logging configuration.

        Keyword Args:
            name (str): The name for the real-time logging configuration.. [optional]
            placement (str, none_type): Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`. . [optional]
            response_condition (str, none_type): The name of an existing condition in the configured endpoint, or leave blank to always execute.. [optional]
            format (str): A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats).. [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
            format_version (int): The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`. . [optional] if omitted the server will use the default value of 2
            message_type (str): How the message should be formatted.. [optional] if omitted the server will use the default value of "classic"
            timestamp_format (str, none_type): A timestamp format. [optional]
            compression_codec (str): The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional]
            period (int): How frequently log files are finalized so they can be available for reading (in seconds).. [optional] if omitted the server will use the default value of 3600
            gzip_level (int): The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error.. [optional] if omitted the server will use the default value of 0
            path (str, none_type): The path to upload logs to.. [optional] if omitted the server will use the default value of "null"
            account_name (str): The unique Azure Blob Storage namespace in which your data objects are stored. Required.. [optional]
            container (str): The name of the Azure Blob Storage container in which to store logs. Required.. [optional]
            sas_token (str): The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required.. [optional]
            public_key (str, none_type): A PGP public key that Fastly will use to encrypt your log files before writing them to disk.. [optional] if omitted the server will use the default value of "null"
            file_max_bytes (int): The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.). [optional]
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
            LoggingAzureblobResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['logging_azureblob_name'] = \
            logging_azureblob_name
        return self.update_log_azure_endpoint.call_with_http_info(**kwargs)

