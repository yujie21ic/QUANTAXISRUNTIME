# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: quotation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='quotation.proto',
  package='QUANTAXIS_Runtime_Quotation',
  syntax='proto3',
  serialized_pb=_b('\n\x0fquotation.proto\x12\x1bQUANTAXIS_Runtime_Quotation\"y\n\rquotation_req\x12\x13\n\x0b\x65xchange_id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x0c\n\x04time\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\"\x8e\x05\n\rquotation_rep\x12\x13\n\x0b\x65xchange_id\x18\x01 \x01(\t\x12\x0e\n\x06ticker\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x12\n\nlast_price\x18\x04 \x01(\x01\x12\x17\n\x0fpre_close_price\x18\x05 \x01(\x01\x12\x0c\n\x04open\x18\x06 \x01(\x01\x12\x0c\n\x04high\x18\x07 \x01(\x01\x12\x0b\n\x03low\x18\x08 \x01(\x01\x12\r\n\x05\x63lose\x18\t \x01(\x01\x12\x13\n\x0b\x63lose_price\x18\n \x01(\x01\x12\x19\n\x11pre_open_interest\x18\x0b \x01(\x01\x12\x15\n\ropen_interest\x18\x0c \x01(\x01\x12\x1c\n\x14pre_settlement_price\x18\r \x01(\x01\x12\x18\n\x10settlement_price\x18\x0e \x01(\x01\x12\x19\n\x11upper_limit_price\x18\x0f \x01(\x01\x12\x19\n\x11lower_limit_price\x18\x10 \x01(\x01\x12\x11\n\tpre_delta\x18\x11 \x01(\x01\x12\x12\n\ncurr_delta\x18\x12 \x01(\x01\x12\x11\n\tdata_time\x18\x13 \x01(\x12\x12\x10\n\x08\x64\x61tetime\x18\x14 \x01(\t\x12\x0b\n\x03qty\x18\x15 \x01(\x12\x12\x0e\n\x06volume\x18\x16 \x01(\x02\x12\x0b\n\x03vol\x18\x17 \x01(\x02\x12\x10\n\x08turnover\x18\x18 \x01(\x01\x12\x11\n\tavg_price\x18\x19 \x01(\x01\x12\x0c\n\x04iopv\x18\x1a \x01(\x01\x12\x15\n\retf_buy_count\x18\x1b \x01(\x11\x12\x16\n\x0e\x65tf_sell_count\x18\x1c \x01(\x11\x12\x13\n\x0b\x65tf_buy_qty\x18\x1d \x01(\x01\x12\x15\n\retf_buy_money\x18\x1e \x01(\x01\x12\x14\n\x0c\x65tf_sell_qty\x18\x1f \x01(\x01\x12\x16\n\x0e\x65tf_sell_money\x18  \x01(\x01\x32\xdf\x02\n\x13QR_QuotationService\x12j\n\x10QR_quotation_p2p\x12*.QUANTAXIS_Runtime_Quotation.quotation_req\x1a*.QUANTAXIS_Runtime_Quotation.quotation_rep\x12l\n\x10QA_quotation_p2s\x12*.QUANTAXIS_Runtime_Quotation.quotation_req\x1a*.QUANTAXIS_Runtime_Quotation.quotation_rep0\x01\x12n\n\x10QA_quotation_s2s\x12*.QUANTAXIS_Runtime_Quotation.quotation_req\x1a*.QUANTAXIS_Runtime_Quotation.quotation_rep(\x01\x30\x01\x62\x06proto3')
)




_QUOTATION_REQ = _descriptor.Descriptor(
  name='quotation_req',
  full_name='QUANTAXIS_Runtime_Quotation.quotation_req',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange_id', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.exchange_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.ip', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.time', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.date', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='QUANTAXIS_Runtime_Quotation.quotation_req.message', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=48,
  serialized_end=169,
)


_QUOTATION_REP = _descriptor.Descriptor(
  name='quotation_rep',
  full_name='QUANTAXIS_Runtime_Quotation.quotation_rep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='exchange_id', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.exchange_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ticker', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.ticker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.code', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.last_price', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_close_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.pre_close_price', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.open', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.high', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.low', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.close', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.close_price', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_open_interest', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.pre_open_interest', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open_interest', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.open_interest', index=11,
      number=12, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_settlement_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.pre_settlement_price', index=12,
      number=13, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='settlement_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.settlement_price', index=13,
      number=14, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='upper_limit_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.upper_limit_price', index=14,
      number=15, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lower_limit_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.lower_limit_price', index=15,
      number=16, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pre_delta', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.pre_delta', index=16,
      number=17, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='curr_delta', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.curr_delta', index=17,
      number=18, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_time', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.data_time', index=18,
      number=19, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='datetime', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.datetime', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qty', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.qty', index=20,
      number=21, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.volume', index=21,
      number=22, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vol', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.vol', index=22,
      number=23, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='turnover', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.turnover', index=23,
      number=24, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avg_price', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.avg_price', index=24,
      number=25, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iopv', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.iopv', index=25,
      number=26, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_buy_count', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_buy_count', index=26,
      number=27, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_sell_count', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_sell_count', index=27,
      number=28, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_buy_qty', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_buy_qty', index=28,
      number=29, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_buy_money', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_buy_money', index=29,
      number=30, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_sell_qty', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_sell_qty', index=30,
      number=31, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='etf_sell_money', full_name='QUANTAXIS_Runtime_Quotation.quotation_rep.etf_sell_money', index=31,
      number=32, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=172,
  serialized_end=826,
)

DESCRIPTOR.message_types_by_name['quotation_req'] = _QUOTATION_REQ
DESCRIPTOR.message_types_by_name['quotation_rep'] = _QUOTATION_REP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

quotation_req = _reflection.GeneratedProtocolMessageType('quotation_req', (_message.Message,), dict(
  DESCRIPTOR = _QUOTATION_REQ,
  __module__ = 'quotation_pb2'
  # @@protoc_insertion_point(class_scope:QUANTAXIS_Runtime_Quotation.quotation_req)
  ))
_sym_db.RegisterMessage(quotation_req)

quotation_rep = _reflection.GeneratedProtocolMessageType('quotation_rep', (_message.Message,), dict(
  DESCRIPTOR = _QUOTATION_REP,
  __module__ = 'quotation_pb2'
  # @@protoc_insertion_point(class_scope:QUANTAXIS_Runtime_Quotation.quotation_rep)
  ))
_sym_db.RegisterMessage(quotation_rep)



_QR_QUOTATIONSERVICE = _descriptor.ServiceDescriptor(
  name='QR_QuotationService',
  full_name='QUANTAXIS_Runtime_Quotation.QR_QuotationService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=829,
  serialized_end=1180,
  methods=[
  _descriptor.MethodDescriptor(
    name='QR_quotation_p2p',
    full_name='QUANTAXIS_Runtime_Quotation.QR_QuotationService.QR_quotation_p2p',
    index=0,
    containing_service=None,
    input_type=_QUOTATION_REQ,
    output_type=_QUOTATION_REP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_quotation_p2s',
    full_name='QUANTAXIS_Runtime_Quotation.QR_QuotationService.QA_quotation_p2s',
    index=1,
    containing_service=None,
    input_type=_QUOTATION_REQ,
    output_type=_QUOTATION_REP,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='QA_quotation_s2s',
    full_name='QUANTAXIS_Runtime_Quotation.QR_QuotationService.QA_quotation_s2s',
    index=2,
    containing_service=None,
    input_type=_QUOTATION_REQ,
    output_type=_QUOTATION_REP,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_QR_QUOTATIONSERVICE)

DESCRIPTOR.services_by_name['QR_QuotationService'] = _QR_QUOTATIONSERVICE

try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class QR_QuotationServiceStub(object):
    """行情服务  无状态的

    参考XTP MarketDataStruct

    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.QR_quotation_p2p = channel.unary_unary(
          '/QUANTAXIS_Runtime_Quotation.QR_QuotationService/QR_quotation_p2p',
          request_serializer=quotation_req.SerializeToString,
          response_deserializer=quotation_rep.FromString,
          )
      self.QA_quotation_p2s = channel.unary_stream(
          '/QUANTAXIS_Runtime_Quotation.QR_QuotationService/QA_quotation_p2s',
          request_serializer=quotation_req.SerializeToString,
          response_deserializer=quotation_rep.FromString,
          )
      self.QA_quotation_s2s = channel.stream_stream(
          '/QUANTAXIS_Runtime_Quotation.QR_QuotationService/QA_quotation_s2s',
          request_serializer=quotation_req.SerializeToString,
          response_deserializer=quotation_rep.FromString,
          )


  class QR_QuotationServiceServicer(object):
    """行情服务  无状态的

    参考XTP MarketDataStruct

    """

    def QR_quotation_p2p(self, request, context):
      """low-level api
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_quotation_p2s(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def QA_quotation_s2s(self, request_iterator, context):
      """rpc QA_fetch_s2p (stream quotation_req) returns (quotation_rep);  // s2p模式没用处
      """
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_QR_QuotationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'QR_quotation_p2p': grpc.unary_unary_rpc_method_handler(
            servicer.QR_quotation_p2p,
            request_deserializer=quotation_req.FromString,
            response_serializer=quotation_rep.SerializeToString,
        ),
        'QA_quotation_p2s': grpc.unary_stream_rpc_method_handler(
            servicer.QA_quotation_p2s,
            request_deserializer=quotation_req.FromString,
            response_serializer=quotation_rep.SerializeToString,
        ),
        'QA_quotation_s2s': grpc.stream_stream_rpc_method_handler(
            servicer.QA_quotation_s2s,
            request_deserializer=quotation_req.FromString,
            response_serializer=quotation_rep.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'QUANTAXIS_Runtime_Quotation.QR_QuotationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaQR_QuotationServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """行情服务  无状态的

    参考XTP MarketDataStruct

    """
    def QR_quotation_p2p(self, request, context):
      """low-level api
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_quotation_p2s(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def QA_quotation_s2s(self, request_iterator, context):
      """rpc QA_fetch_s2p (stream quotation_req) returns (quotation_rep);  // s2p模式没用处
      """
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaQR_QuotationServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """行情服务  无状态的

    参考XTP MarketDataStruct

    """
    def QR_quotation_p2p(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      """low-level api
      """
      raise NotImplementedError()
    QR_quotation_p2p.future = None
    def QA_quotation_p2s(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    def QA_quotation_s2s(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
      """rpc QA_fetch_s2p (stream quotation_req) returns (quotation_rep);  // s2p模式没用处
      """
      raise NotImplementedError()


  def beta_create_QR_QuotationService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_p2s'): quotation_req.FromString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_s2s'): quotation_req.FromString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QR_quotation_p2p'): quotation_req.FromString,
    }
    response_serializers = {
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_p2s'): quotation_rep.SerializeToString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_s2s'): quotation_rep.SerializeToString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QR_quotation_p2p'): quotation_rep.SerializeToString,
    }
    method_implementations = {
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_p2s'): face_utilities.unary_stream_inline(servicer.QA_quotation_p2s),
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_s2s'): face_utilities.stream_stream_inline(servicer.QA_quotation_s2s),
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QR_quotation_p2p'): face_utilities.unary_unary_inline(servicer.QR_quotation_p2p),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_QR_QuotationService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_p2s'): quotation_req.SerializeToString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_s2s'): quotation_req.SerializeToString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QR_quotation_p2p'): quotation_req.SerializeToString,
    }
    response_deserializers = {
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_p2s'): quotation_rep.FromString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QA_quotation_s2s'): quotation_rep.FromString,
      ('QUANTAXIS_Runtime_Quotation.QR_QuotationService', 'QR_quotation_p2p'): quotation_rep.FromString,
    }
    cardinalities = {
      'QA_quotation_p2s': cardinality.Cardinality.UNARY_STREAM,
      'QA_quotation_s2s': cardinality.Cardinality.STREAM_STREAM,
      'QR_quotation_p2p': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'QUANTAXIS_Runtime_Quotation.QR_QuotationService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
