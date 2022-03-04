"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......proto.api.common.v1 import common_pb2 as proto_dot_api_dot_common_dot_v1_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*proto/api/service/sensors/v1/sensors.proto\x12\x1cproto.api.service.sensors.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1cgoogle/api/annotations.proto\x1a proto/api/common/v1/common.proto"\x13\n\x11GetSensorsRequest"Z\n\x12GetSensorsResponse\x12D\n\x0csensor_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\x0bsensorNames"Z\n\x12GetReadingsRequest\x12D\n\x0csensor_names\x18\x01 \x03(\x0b2!.proto.api.common.v1.ResourceNameR\x0bsensorNames"u\n\x08Readings\x125\n\x04name\x18\x01 \x01(\x0b2!.proto.api.common.v1.ResourceNameR\x04name\x122\n\x08readings\x18\x02 \x03(\x0b2\x16.google.protobuf.ValueR\x08readings"Y\n\x13GetReadingsResponse\x12B\n\x08readings\x18\x01 \x03(\x0b2&.proto.api.service.sensors.v1.ReadingsR\x08readings2\xc2\x02\n\x0eSensorsService\x12\x90\x01\n\nGetSensors\x12/.proto.api.service.sensors.v1.GetSensorsRequest\x1a0.proto.api.service.sensors.v1.GetSensorsResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/api/v1/service/sensors\x12\x9c\x01\n\x0bGetReadings\x120.proto.api.service.sensors.v1.GetReadingsRequest\x1a1.proto.api.service.sensors.v1.GetReadingsResponse"(\x82\xd3\xe4\x93\x02"\x12 /api/v1/service/sensors/readingsBY\n)com.viam.rdk.proto.api.service.sensors.v1Z,go.viam.com/rdk/proto/api/service/sensors/v1b\x06proto3')
_GETSENSORSREQUEST = DESCRIPTOR.message_types_by_name['GetSensorsRequest']
_GETSENSORSRESPONSE = DESCRIPTOR.message_types_by_name['GetSensorsResponse']
_GETREADINGSREQUEST = DESCRIPTOR.message_types_by_name['GetReadingsRequest']
_READINGS = DESCRIPTOR.message_types_by_name['Readings']
_GETREADINGSRESPONSE = DESCRIPTOR.message_types_by_name['GetReadingsResponse']
GetSensorsRequest = _reflection.GeneratedProtocolMessageType('GetSensorsRequest', (_message.Message,), {'DESCRIPTOR': _GETSENSORSREQUEST, '__module__': 'proto.api.service.sensors.v1.sensors_pb2'})
_sym_db.RegisterMessage(GetSensorsRequest)
GetSensorsResponse = _reflection.GeneratedProtocolMessageType('GetSensorsResponse', (_message.Message,), {'DESCRIPTOR': _GETSENSORSRESPONSE, '__module__': 'proto.api.service.sensors.v1.sensors_pb2'})
_sym_db.RegisterMessage(GetSensorsResponse)
GetReadingsRequest = _reflection.GeneratedProtocolMessageType('GetReadingsRequest', (_message.Message,), {'DESCRIPTOR': _GETREADINGSREQUEST, '__module__': 'proto.api.service.sensors.v1.sensors_pb2'})
_sym_db.RegisterMessage(GetReadingsRequest)
Readings = _reflection.GeneratedProtocolMessageType('Readings', (_message.Message,), {'DESCRIPTOR': _READINGS, '__module__': 'proto.api.service.sensors.v1.sensors_pb2'})
_sym_db.RegisterMessage(Readings)
GetReadingsResponse = _reflection.GeneratedProtocolMessageType('GetReadingsResponse', (_message.Message,), {'DESCRIPTOR': _GETREADINGSRESPONSE, '__module__': 'proto.api.service.sensors.v1.sensors_pb2'})
_sym_db.RegisterMessage(GetReadingsResponse)
_SENSORSSERVICE = DESCRIPTOR.services_by_name['SensorsService']
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n)com.viam.rdk.proto.api.service.sensors.v1Z,go.viam.com/rdk/proto/api/service/sensors/v1'
    _SENSORSSERVICE.methods_by_name['GetSensors']._options = None
    _SENSORSSERVICE.methods_by_name['GetSensors']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/api/v1/service/sensors'
    _SENSORSSERVICE.methods_by_name['GetReadings']._options = None
    _SENSORSSERVICE.methods_by_name['GetReadings']._serialized_options = b'\x82\xd3\xe4\x93\x02"\x12 /api/v1/service/sensors/readings'
    _GETSENSORSREQUEST._serialized_start = 170
    _GETSENSORSREQUEST._serialized_end = 189
    _GETSENSORSRESPONSE._serialized_start = 191
    _GETSENSORSRESPONSE._serialized_end = 281
    _GETREADINGSREQUEST._serialized_start = 283
    _GETREADINGSREQUEST._serialized_end = 373
    _READINGS._serialized_start = 375
    _READINGS._serialized_end = 492
    _GETREADINGSRESPONSE._serialized_start = 494
    _GETREADINGSRESPONSE._serialized_end = 583
    _SENSORSSERVICE._serialized_start = 586
    _SENSORSSERVICE._serialized_end = 908