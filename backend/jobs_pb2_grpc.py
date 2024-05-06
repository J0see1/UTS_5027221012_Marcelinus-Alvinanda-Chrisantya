# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import jobs_pb2 as jobs__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in jobs_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class JobServiceStub(object):
    """Service 
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddJob = channel.unary_unary(
                '/JobService/AddJob',
                request_serializer=jobs__pb2.Job.SerializeToString,
                response_deserializer=jobs__pb2.Job.FromString,
                _registered_method=True)
        self.GetAll = channel.unary_unary(
                '/JobService/GetAll',
                request_serializer=jobs__pb2.Empty.SerializeToString,
                response_deserializer=jobs__pb2.JobList.FromString,
                _registered_method=True)
        self.GetJob = channel.unary_unary(
                '/JobService/GetJob',
                request_serializer=jobs__pb2.JobTitle.SerializeToString,
                response_deserializer=jobs__pb2.Job.FromString,
                _registered_method=True)
        self.UpdateJob = channel.unary_unary(
                '/JobService/UpdateJob',
                request_serializer=jobs__pb2.Job.SerializeToString,
                response_deserializer=jobs__pb2.Job.FromString,
                _registered_method=True)
        self.DeleteJob = channel.unary_unary(
                '/JobService/DeleteJob',
                request_serializer=jobs__pb2.JobId.SerializeToString,
                response_deserializer=jobs__pb2.Empty.FromString,
                _registered_method=True)


class JobServiceServicer(object):
    """Service 
    """

    def AddJob(self, request, context):
        """Create
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAll(self, request, context):
        """Read 
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJob(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateJob(self, request, context):
        """Update
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteJob(self, request, context):
        """Delete
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_JobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddJob': grpc.unary_unary_rpc_method_handler(
                    servicer.AddJob,
                    request_deserializer=jobs__pb2.Job.FromString,
                    response_serializer=jobs__pb2.Job.SerializeToString,
            ),
            'GetAll': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAll,
                    request_deserializer=jobs__pb2.Empty.FromString,
                    response_serializer=jobs__pb2.JobList.SerializeToString,
            ),
            'GetJob': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJob,
                    request_deserializer=jobs__pb2.JobTitle.FromString,
                    response_serializer=jobs__pb2.Job.SerializeToString,
            ),
            'UpdateJob': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateJob,
                    request_deserializer=jobs__pb2.Job.FromString,
                    response_serializer=jobs__pb2.Job.SerializeToString,
            ),
            'DeleteJob': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteJob,
                    request_deserializer=jobs__pb2.JobId.FromString,
                    response_serializer=jobs__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'JobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class JobService(object):
    """Service 
    """

    @staticmethod
    def AddJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/JobService/AddJob',
            jobs__pb2.Job.SerializeToString,
            jobs__pb2.Job.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetAll(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/JobService/GetAll',
            jobs__pb2.Empty.SerializeToString,
            jobs__pb2.JobList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/JobService/GetJob',
            jobs__pb2.JobTitle.SerializeToString,
            jobs__pb2.Job.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/JobService/UpdateJob',
            jobs__pb2.Job.SerializeToString,
            jobs__pb2.Job.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteJob(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/JobService/DeleteJob',
            jobs__pb2.JobId.SerializeToString,
            jobs__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
