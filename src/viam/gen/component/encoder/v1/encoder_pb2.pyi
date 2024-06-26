"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing
if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _PositionType:
    ValueType = typing.NewType('ValueType', builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _PositionTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_PositionType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    POSITION_TYPE_UNSPECIFIED: _PositionType.ValueType
    POSITION_TYPE_TICKS_COUNT: _PositionType.ValueType
    "Return type for relative encoders that report\n    how far they've gone from a start position\n    "
    POSITION_TYPE_ANGLE_DEGREES: _PositionType.ValueType
    'Return type for absolute encoders that report\n    their position in degrees along the radial axis\n    '

class PositionType(_PositionType, metaclass=_PositionTypeEnumTypeWrapper):
    ...
POSITION_TYPE_UNSPECIFIED: PositionType.ValueType
POSITION_TYPE_TICKS_COUNT: PositionType.ValueType
"Return type for relative encoders that report\nhow far they've gone from a start position\n"
POSITION_TYPE_ANGLE_DEGREES: PositionType.ValueType
'Return type for absolute encoders that report\ntheir position in degrees along the radial axis\n'
global___PositionType = PositionType

@typing.final
class GetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    POSITION_TYPE_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of encoder'
    position_type: global___PositionType.ValueType
    'If supplied, the response will return the specified\n    position type. If the driver does not implement\n    the requested type, this call will return an error.\n    If position type is not specified, the response\n    will return a default according to the driver.\n    '

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., position_type: global___PositionType.ValueType | None=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['_position_type', b'_position_type', 'extra', b'extra', 'position_type', b'position_type']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['_position_type', b'_position_type', 'extra', b'extra', 'name', b'name', 'position_type', b'position_type']) -> None:
        ...

    def WhichOneof(self, oneof_group: typing.Literal['_position_type', b'_position_type']) -> typing.Literal['position_type'] | None:
        ...
global___GetPositionRequest = GetPositionRequest

@typing.final
class GetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: builtins.int
    POSITION_TYPE_FIELD_NUMBER: builtins.int
    value: builtins.float
    position_type: global___PositionType.ValueType

    def __init__(self, *, value: builtins.float=..., position_type: global___PositionType.ValueType=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['position_type', b'position_type', 'value', b'value']) -> None:
        ...
global___GetPositionResponse = GetPositionResponse

@typing.final
class ResetPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of an encoder'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___ResetPositionRequest = ResetPositionRequest

@typing.final
class ResetPositionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(self) -> None:
        ...
global___ResetPositionResponse = ResetPositionResponse

@typing.final
class GetPropertiesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: builtins.int
    EXTRA_FIELD_NUMBER: builtins.int
    name: builtins.str
    'Name of the encoder'

    @property
    def extra(self) -> google.protobuf.struct_pb2.Struct:
        """Additional arguments to the method"""

    def __init__(self, *, name: builtins.str=..., extra: google.protobuf.struct_pb2.Struct | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['extra', b'extra']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['extra', b'extra', 'name', b'name']) -> None:
        ...
global___GetPropertiesRequest = GetPropertiesRequest

@typing.final
class GetPropertiesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TICKS_COUNT_SUPPORTED_FIELD_NUMBER: builtins.int
    ANGLE_DEGREES_SUPPORTED_FIELD_NUMBER: builtins.int
    ticks_count_supported: builtins.bool
    angle_degrees_supported: builtins.bool

    def __init__(self, *, ticks_count_supported: builtins.bool=..., angle_degrees_supported: builtins.bool=...) -> None:
        ...

    def ClearField(self, field_name: typing.Literal['angle_degrees_supported', b'angle_degrees_supported', 'ticks_count_supported', b'ticks_count_supported']) -> None:
        ...
global___GetPropertiesResponse = GetPropertiesResponse