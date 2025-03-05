"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
from .... import app
import builtins
import google.protobuf.descriptor
import google.protobuf.message
from .... import service
import typing
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetInferenceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    REGISTRY_ITEM_ID_FIELD_NUMBER: builtins.int
    REGISTRY_ITEM_VERSION_FIELD_NUMBER: builtins.int
    BINARY_ID_FIELD_NUMBER: builtins.int
    BINARY_DATA_ID_FIELD_NUMBER: builtins.int
    ORGANIZATION_ID_FIELD_NUMBER: builtins.int
    registry_item_id: builtins.str
    'The model framework and model type are inferred from the ML model registry item;\n    For valid model types (classification, detections) we will return the formatted\n    labels or annotations from the associated inference outputs.\n    '
    registry_item_version: builtins.str
    binary_data_id: builtins.str
    organization_id: builtins.str

    @property
    def binary_id(self) -> app.data.v1.data_pb2.BinaryID:
        ...

    def __init__(self, *, registry_item_id: builtins.str=..., registry_item_version: builtins.str=..., binary_id: app.data.v1.data_pb2.BinaryID | None=..., binary_data_id: builtins.str=..., organization_id: builtins.str=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['binary_id', b'binary_id']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['binary_data_id', b'binary_data_id', 'binary_id', b'binary_id', 'organization_id', b'organization_id', 'registry_item_id', b'registry_item_id', 'registry_item_version', b'registry_item_version']) -> None:
        ...
global___GetInferenceRequest = GetInferenceRequest

@typing.final
class GetInferenceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OUTPUT_TENSORS_FIELD_NUMBER: builtins.int
    ANNOTATIONS_FIELD_NUMBER: builtins.int

    @property
    def output_tensors(self) -> service.mlmodel.v1.mlmodel_pb2.FlatTensors:
        ...

    @property
    def annotations(self) -> app.data.v1.data_pb2.Annotations:
        ...

    def __init__(self, *, output_tensors: service.mlmodel.v1.mlmodel_pb2.FlatTensors | None=..., annotations: app.data.v1.data_pb2.Annotations | None=...) -> None:
        ...

    def HasField(self, field_name: typing.Literal['annotations', b'annotations', 'output_tensors', b'output_tensors']) -> builtins.bool:
        ...

    def ClearField(self, field_name: typing.Literal['annotations', b'annotations', 'output_tensors', b'output_tensors']) -> None:
        ...
global___GetInferenceResponse = GetInferenceResponse