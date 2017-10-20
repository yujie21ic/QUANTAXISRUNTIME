# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock_hq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import stock_min_pb2 as stock__min__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock_hq.proto',
  package='stock_hq',
  syntax='proto3',
  serialized_pb=_b('\n\x0estock_hq.proto\x12\x08stock_hq\x1a\x0fstock_min.proto\"#\n\x05Query\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t2A\n\x0eStockHQService\x12/\n\x0cQA_fetch_get\x12\x0f.stock_hq.Query\x1a\n.stock_min(\x01\x30\x01\x62\x06proto3')
  ,
  dependencies=[stock__min__pb2.DESCRIPTOR,])




_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='stock_hq.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='stock_hq.Query.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='stock_hq.Query.code', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['Query'] = _QUERY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'stock_hq_pb2'
  # @@protoc_insertion_point(class_scope:stock_hq.Query)
  ))
_sym_db.RegisterMessage(Query)



_STOCKHQSERVICE = _descriptor.ServiceDescriptor(
  name='StockHQService',
  full_name='stock_hq.StockHQService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=82,
  serialized_end=147,
  methods=[
  _descriptor.MethodDescriptor(
    name='QA_fetch_get',
    full_name='stock_hq.StockHQService.QA_fetch_get',
    index=0,
    containing_service=None,
    input_type=_QUERY,
    output_type=stock__min__pb2._STOCK_MIN,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STOCKHQSERVICE)

DESCRIPTOR.services_by_name['StockHQService'] = _STOCKHQSERVICE

# @@protoc_insertion_point(module_scope)
