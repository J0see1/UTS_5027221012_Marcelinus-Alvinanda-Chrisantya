# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: jobs.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\njobs.proto\"S\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ompany\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0e\n\x06salary\x18\x05 \x01(\x03\"\x1d\n\x07JobList\x12\x12\n\x04jobs\x18\x01 \x03(\x0b\x32\x04.Job\"\x13\n\x05JobId\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\x96\x01\n\nJobService\x12\x16\n\x06\x41\x64\x64Job\x12\x04.Job\x1a\x04.Job\"\x00\x12\x1c\n\x06GetAll\x12\x06.Empty\x1a\x08.JobList\"\x00\x12\x18\n\x06GetJob\x12\x06.JobId\x1a\x04.Job\"\x00\x12\x19\n\tUpdateJob\x12\x04.Job\x1a\x04.Job\"\x00\x12\x1d\n\tDeleteJob\x12\x06.JobId\x1a\x06.Empty\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'jobs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_JOB']._serialized_start=14
  _globals['_JOB']._serialized_end=97
  _globals['_JOBLIST']._serialized_start=99
  _globals['_JOBLIST']._serialized_end=128
  _globals['_JOBID']._serialized_start=130
  _globals['_JOBID']._serialized_end=149
  _globals['_EMPTY']._serialized_start=151
  _globals['_EMPTY']._serialized_end=158
  _globals['_JOBSERVICE']._serialized_start=161
  _globals['_JOBSERVICE']._serialized_end=311
# @@protoc_insertion_point(module_scope)
