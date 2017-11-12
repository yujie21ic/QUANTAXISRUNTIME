# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import stock_hq_pb2 as stock__hq__pb2


class StockHQServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.QA_fetch_p2p = channel.unary_unary(
        '/stock_hq.StockHQService/QA_fetch_p2p',
        request_serializer=stock__hq__pb2.query_struct.SerializeToString,
        response_deserializer=stock__hq__pb2.hq_struct.FromString,
        )
    self.QA_fetch_p2s = channel.unary_stream(
        '/stock_hq.StockHQService/QA_fetch_p2s',
        request_serializer=stock__hq__pb2.query_struct.SerializeToString,
        response_deserializer=stock__hq__pb2.hq_struct.FromString,
        )
    self.QA_fetch_s2s = channel.stream_stream(
        '/stock_hq.StockHQService/QA_fetch_s2s',
        request_serializer=stock__hq__pb2.query_struct.SerializeToString,
        response_deserializer=stock__hq__pb2.hq_struct.FromString,
        )
    self.QA_fetch_s2p = channel.stream_unary(
        '/stock_hq.StockHQService/QA_fetch_s2p',
        request_serializer=stock__hq__pb2.query_struct.SerializeToString,
        response_deserializer=stock__hq__pb2.hq_struct.FromString,
        )
    self.QA_fetch_realtime = channel.unary_stream(
        '/stock_hq.StockHQService/QA_fetch_realtime',
        request_serializer=stock__hq__pb2.query_realtime.SerializeToString,
        response_deserializer=stock__hq__pb2.hq_struct.FromString,
        )


class StockHQServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def QA_fetch_p2p(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QA_fetch_p2s(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QA_fetch_s2s(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QA_fetch_s2p(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QA_fetch_realtime(self, request, context):
    """rpc RouteChat (stream long) returns (stream long_hq);
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_StockHQServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'QA_fetch_p2p': grpc.unary_unary_rpc_method_handler(
          servicer.QA_fetch_p2p,
          request_deserializer=stock__hq__pb2.query_struct.FromString,
          response_serializer=stock__hq__pb2.hq_struct.SerializeToString,
      ),
      'QA_fetch_p2s': grpc.unary_stream_rpc_method_handler(
          servicer.QA_fetch_p2s,
          request_deserializer=stock__hq__pb2.query_struct.FromString,
          response_serializer=stock__hq__pb2.hq_struct.SerializeToString,
      ),
      'QA_fetch_s2s': grpc.stream_stream_rpc_method_handler(
          servicer.QA_fetch_s2s,
          request_deserializer=stock__hq__pb2.query_struct.FromString,
          response_serializer=stock__hq__pb2.hq_struct.SerializeToString,
      ),
      'QA_fetch_s2p': grpc.stream_unary_rpc_method_handler(
          servicer.QA_fetch_s2p,
          request_deserializer=stock__hq__pb2.query_struct.FromString,
          response_serializer=stock__hq__pb2.hq_struct.SerializeToString,
      ),
      'QA_fetch_realtime': grpc.unary_stream_rpc_method_handler(
          servicer.QA_fetch_realtime,
          request_deserializer=stock__hq__pb2.query_realtime.FromString,
          response_serializer=stock__hq__pb2.hq_struct.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'stock_hq.StockHQService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))