# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='message.proto',
  package='',
  serialized_pb=b'\n\rmessage.proto\"\x14\n\x04User\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1b\n\x0b\x45\x63hoRequest\x12\x0c\n\x04\x65\x63ho\x18\x01 \x02(\t\"\x1c\n\x0c\x45\x63hoResponse\x12\x0c\n\x04\x65\x63ho\x18\x01 \x02(\t\"\"\n\nAddRequest\x12\t\n\x01\x61\x18\x01 \x02(\x05\x12\t\n\x01\x62\x18\x02 \x02(\x05\"\x1d\n\x0b\x41\x64\x64Response\x12\x0e\n\x06result\x18\x01 \x02(\x05\"\x1e\n\rSearchRequest\x12\r\n\x05query\x18\x01 \x02(\t\"&\n\x0eSearchResponse\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User')




_USER = descriptor.Descriptor(
  name='User',
  full_name='User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='User.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
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
  extension_ranges=[],
  serialized_start=17,
  serialized_end=37,
)


_ECHOREQUEST = descriptor.Descriptor(
  name='EchoRequest',
  full_name='EchoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='echo', full_name='EchoRequest.echo', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
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
  extension_ranges=[],
  serialized_start=39,
  serialized_end=66,
)


_ECHORESPONSE = descriptor.Descriptor(
  name='EchoResponse',
  full_name='EchoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='echo', full_name='EchoResponse.echo', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
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
  extension_ranges=[],
  serialized_start=68,
  serialized_end=96,
)


_ADDREQUEST = descriptor.Descriptor(
  name='AddRequest',
  full_name='AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='a', full_name='AddRequest.a', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='b', full_name='AddRequest.b', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=98,
  serialized_end=132,
)


_ADDRESPONSE = descriptor.Descriptor(
  name='AddResponse',
  full_name='AddResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='result', full_name='AddResponse.result', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  extension_ranges=[],
  serialized_start=134,
  serialized_end=163,
)


_SEARCHREQUEST = descriptor.Descriptor(
  name='SearchRequest',
  full_name='SearchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='query', full_name='SearchRequest.query', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode("utf-8"),
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
  extension_ranges=[],
  serialized_start=165,
  serialized_end=195,
)


_SEARCHRESPONSE = descriptor.Descriptor(
  name='SearchResponse',
  full_name='SearchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='users', full_name='SearchResponse.users', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  extension_ranges=[],
  serialized_start=197,
  serialized_end=235,
)

_SEARCHRESPONSE.fields_by_name['users'].message_type = _USER
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['EchoRequest'] = _ECHOREQUEST
DESCRIPTOR.message_types_by_name['EchoResponse'] = _ECHORESPONSE
DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddResponse'] = _ADDRESPONSE
DESCRIPTOR.message_types_by_name['SearchRequest'] = _SEARCHREQUEST
DESCRIPTOR.message_types_by_name['SearchResponse'] = _SEARCHRESPONSE

User = reflection.GeneratedProtocolMessageType('User', (message.Message,),
    {
      'DESCRIPTOR': _USER,
      # @@protoc_insertion_point(class_scope:User)
    })

EchoRequest = reflection.GeneratedProtocolMessageType('EchoRequest', (message.Message,),
    {
      'DESCRIPTOR': _ECHOREQUEST,
      # @@protoc_insertion_point(class_scope:EchoRequest)
    })

EchoResponse = reflection.GeneratedProtocolMessageType('EchoResponse', (message.Message,),
    {
      'DESCRIPTOR': _ECHORESPONSE,
      # @@protoc_insertion_point(class_scope:EchoResponse)
    })

AddRequest = reflection.GeneratedProtocolMessageType('AddRequest', (message.Message,),
    {
      'DESCRIPTOR': _ADDREQUEST,
      # @@protoc_insertion_point(class_scope:AddRequest)
    })

AddResponse = reflection.GeneratedProtocolMessageType('AddResponse', (message.Message,),
    {
      'DESCRIPTOR': _ADDRESPONSE,
      # @@protoc_insertion_point(class_scope:AddResponse)
    })

SearchRequest = reflection.GeneratedProtocolMessageType('SearchRequest', (message.Message,),
    {
      'DESCRIPTOR': _SEARCHREQUEST,
      # @@protoc_insertion_point(class_scope:SearchRequest)
    })

SearchResponse = reflection.GeneratedProtocolMessageType('SearchResponse', (message.Message,),
    {
      'DESCRIPTOR': _SEARCHRESPONSE,
      # @@protoc_insertion_point(class_scope:SearchResponse)
    })

# @@protoc_insertion_point(module_scope)