# Copyright 2023-2024, NVIDIA CORPORATION & AFFILIATES. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Type information for Triton _c bindings."""

# Note: this file was generated using mypy with an empty __init__.py
# file in the tritonserver package directory to avoid any renaming /
# aliasing done by the wrapper
#
# mypy 1.8.0 (compiled: yes)
#
# stubgen -p tritonserver._c
#
# Todo: add stub generation to build process

import numpy
from typing import Callable, ClassVar, List, Optional, Tuple, overload

ALL: TRITONSERVER_RequestReleaseFlag
COMPUTE_END: TRITONSERVER_InferenceTraceActivity
COMPUTE_INPUT_END: TRITONSERVER_InferenceTraceActivity
COMPUTE_OUTPUT_START: TRITONSERVER_InferenceTraceActivity
COMPUTE_START: TRITONSERVER_InferenceTraceActivity
DECOUPLED: TRITONSERVER_ModelTxnPropertyFlag
DISABLED: TRITONSERVER_InferenceTraceLevel
FINAL: TRITONSERVER_ResponseCompleteFlag
FIRST_DIM: TRITONSERVER_ModelBatchFlag
MAX: TRITONSERVER_InferenceTraceLevel
MIN: TRITONSERVER_InferenceTraceLevel
ONE_TO_ONE: TRITONSERVER_ModelTxnPropertyFlag
QUEUE_START: TRITONSERVER_InferenceTraceActivity
READY: TRITONSERVER_ModelIndexFlag
REQUEST_END: TRITONSERVER_InferenceTraceActivity
REQUEST_START: TRITONSERVER_InferenceTraceActivity
SEQUENCE_END: TRITONSERVER_RequestFlag
SEQUENCE_START: TRITONSERVER_RequestFlag
TENSORS: TRITONSERVER_InferenceTraceLevel
TENSOR_BACKEND_INPUT: TRITONSERVER_InferenceTraceActivity
TENSOR_BACKEND_OUTPUT: TRITONSERVER_InferenceTraceActivity
TENSOR_QUEUE_INPUT: TRITONSERVER_InferenceTraceActivity
TIMESTAMPS: TRITONSERVER_InferenceTraceLevel
UNKNOWN: TRITONSERVER_ModelBatchFlag

class AlreadyExistsError(TritonError): ...
class InternalError(TritonError): ...
class InvalidArgumentError(TritonError): ...
class NotFoundError(TritonError): ...

class TRITONSERVER_BufferAttributes:
    byte_size: int
    cuda_ipc_handle: int
    memory_type: TRITONSERVER_MemoryType
    memory_type_id: int
    def __init__(self) -> None: ...

class TRITONSERVER_DataType:
    __members__: ClassVar[dict] = ...  # read-only
    BF16: ClassVar[TRITONSERVER_DataType] = ...
    BOOL: ClassVar[TRITONSERVER_DataType] = ...
    BYTES: ClassVar[TRITONSERVER_DataType] = ...
    FP16: ClassVar[TRITONSERVER_DataType] = ...
    FP32: ClassVar[TRITONSERVER_DataType] = ...
    FP64: ClassVar[TRITONSERVER_DataType] = ...
    INT16: ClassVar[TRITONSERVER_DataType] = ...
    INT32: ClassVar[TRITONSERVER_DataType] = ...
    INT64: ClassVar[TRITONSERVER_DataType] = ...
    INT8: ClassVar[TRITONSERVER_DataType] = ...
    INVALID: ClassVar[TRITONSERVER_DataType] = ...
    UINT16: ClassVar[TRITONSERVER_DataType] = ...
    UINT32: ClassVar[TRITONSERVER_DataType] = ...
    UINT64: ClassVar[TRITONSERVER_DataType] = ...
    UINT8: ClassVar[TRITONSERVER_DataType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_InferenceRequest:
    correlation_id: int
    correlation_id_string: str
    flags: int
    id: str
    priority: int
    priority_uint64: int
    timeout_microseconds: int
    def __init__(self, arg0, arg1: str, arg2: int) -> None: ...
    def add_input(
        self, arg0: str, arg1: TRITONSERVER_DataType, arg2: List[int]
    ) -> None: ...
    def add_raw_input(self, arg0: str) -> None: ...
    def add_requested_output(self, arg0: str) -> None: ...
    def append_input_data(
        self, arg0: str, arg1: int, arg2: int, arg3: TRITONSERVER_MemoryType, arg4: int
    ) -> None: ...
    def append_input_data_with_buffer_attributes(
        self, arg0: str, arg1: int, arg2: TRITONSERVER_BufferAttributes
    ) -> None: ...
    def append_input_data_with_host_policy(
        self,
        arg0: str,
        arg1: int,
        arg2: int,
        arg3: TRITONSERVER_MemoryType,
        arg4: int,
        arg5: str,
    ) -> None: ...
    def cancel(self) -> None: ...
    def remove_all_input_data(self, arg0: str) -> None: ...
    def remove_all_inputs(self) -> None: ...
    def remove_all_requested_outputs(self) -> None: ...
    def remove_input(self, arg0: str) -> None: ...
    def remove_requested_output(self, arg0: str) -> None: ...
    def set_bool_parameter(self, arg0: str, arg1: bool) -> None: ...
    def set_int_parameter(self, arg0: str, arg1: int) -> None: ...
    def set_release_callback(
        self,
        arg0: Callable[[TRITONSERVER_InferenceRequest, int, object], None],
        arg1: object,
    ) -> None: ...
    def set_response_callback(
        self,
        arg0: object,
        arg1: object,
        arg2: Callable[[object, int, object], None],
        arg3: object,
    ) -> None: ...
    def set_string_parameter(self, arg0: str, arg1: str) -> None: ...

class TRITONSERVER_InferenceResponse:
    def __init__(self, *args, **kwargs) -> None: ...
    def output(
        self, arg0: int
    ) -> Tuple[
        str,
        TRITONSERVER_DataType,
        numpy.ndarray[numpy.int64],
        int,
        int,
        TRITONSERVER_MemoryType,
        int,
        object,
    ]: ...
    def output_classification_label(self, arg0: int, arg1: int) -> str: ...
    def parameter(
        self, arg0: int
    ) -> Tuple[str, TRITONSERVER_ParameterType, object]: ...
    def throw_if_response_error(self) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def model(self) -> Tuple[str, int]: ...
    @property
    def output_count(self) -> int: ...
    @property
    def parameter_count(self) -> int: ...

class TRITONSERVER_InferenceTrace:
    @overload
    def __init__(
        self,
        level: int,
        parent_id: int,
        activity_function: Callable[
            [object, TRITONSERVER_InferenceTraceActivity, int, object], None
        ],
        tensor_activity_function: Callable[
            [
                object,
                TRITONSERVER_InferenceTraceActivity,
                str,
                TRITONSERVER_DataType,
                int,
                int,
                numpy.ndarray[numpy.int64],
                TRITONSERVER_MemoryType,
                int,
                object,
            ],
            None,
        ],
        release_function: Callable[[TRITONSERVER_InferenceTrace, object], None],
        trace_userp: object,
    ) -> None: ...
    @overload
    def __init__(
        self,
        level: int,
        parent_id: int,
        activity_function: Callable[
            [object, TRITONSERVER_InferenceTraceActivity, int, object], None
        ],
        release_function: Callable[[TRITONSERVER_InferenceTrace, object], None],
        trace_userp: object,
    ) -> None: ...
    @property
    def id(self) -> int: ...
    @property
    def model_name(self) -> str: ...
    @property
    def model_version(self) -> int: ...
    @property
    def parent_id(self) -> int: ...
    @property
    def request_id(self) -> str: ...

class TRITONSERVER_InferenceTraceActivity:
    __members__: ClassVar[dict] = ...  # read-only
    COMPUTE_END: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    COMPUTE_INPUT_END: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    COMPUTE_OUTPUT_START: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    COMPUTE_START: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    QUEUE_START: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    REQUEST_END: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    REQUEST_START: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    TENSOR_BACKEND_INPUT: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    TENSOR_BACKEND_OUTPUT: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    TENSOR_QUEUE_INPUT: ClassVar[TRITONSERVER_InferenceTraceActivity] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_InferenceTraceLevel:
    __members__: ClassVar[dict] = ...  # read-only
    DISABLED: ClassVar[TRITONSERVER_InferenceTraceLevel] = ...
    MAX: ClassVar[TRITONSERVER_InferenceTraceLevel] = ...
    MIN: ClassVar[TRITONSERVER_InferenceTraceLevel] = ...
    TENSORS: ClassVar[TRITONSERVER_InferenceTraceLevel] = ...
    TIMESTAMPS: ClassVar[TRITONSERVER_InferenceTraceLevel] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_InstanceGroupKind:
    __members__: ClassVar[dict] = ...  # read-only
    AUTO: ClassVar[TRITONSERVER_InstanceGroupKind] = ...
    CPU: ClassVar[TRITONSERVER_InstanceGroupKind] = ...
    GPU: ClassVar[TRITONSERVER_InstanceGroupKind] = ...
    MODEL: ClassVar[TRITONSERVER_InstanceGroupKind] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_LogFormat:
    __members__: ClassVar[dict] = ...  # read-only
    DEFAULT: ClassVar[TRITONSERVER_LogFormat] = ...
    ISO8601: ClassVar[TRITONSERVER_LogFormat] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_LogLevel:
    __members__: ClassVar[dict] = ...  # read-only
    ERROR: ClassVar[TRITONSERVER_LogLevel] = ...
    INFO: ClassVar[TRITONSERVER_LogLevel] = ...
    VERBOSE: ClassVar[TRITONSERVER_LogLevel] = ...
    WARN: ClassVar[TRITONSERVER_LogLevel] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_MemoryType:
    __members__: ClassVar[dict] = ...  # read-only
    CPU: ClassVar[TRITONSERVER_MemoryType] = ...
    CPU_PINNED: ClassVar[TRITONSERVER_MemoryType] = ...
    GPU: ClassVar[TRITONSERVER_MemoryType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_Message:
    def __init__(self, arg0: str) -> None: ...
    def serialize_to_json(self) -> str: ...

class TRITONSERVER_Metric:
    def __init__(
        self, arg0: TRITONSERVER_MetricFamily, arg1: List[TRITONSERVER_Parameter]
    ) -> None: ...
    def increment(self, arg0: float) -> None: ...
    def set_value(self, arg0: float) -> None: ...
    @property
    def kind(self) -> TRITONSERVER_MetricKind: ...
    @property
    def value(self) -> float: ...

class TRITONSERVER_MetricFamily:
    def __init__(self, arg0: TRITONSERVER_MetricKind, arg1: str, arg2: str) -> None: ...

class TRITONSERVER_MetricFormat:
    __members__: ClassVar[dict] = ...  # read-only
    PROMETHEUS: ClassVar[TRITONSERVER_MetricFormat] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_MetricKind:
    __members__: ClassVar[dict] = ...  # read-only
    COUNTER: ClassVar[TRITONSERVER_MetricKind] = ...
    GAUGE: ClassVar[TRITONSERVER_MetricKind] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_Metrics:
    def __init__(self, *args, **kwargs) -> None: ...
    def formatted(self, arg0: TRITONSERVER_MetricFormat) -> str: ...

class TRITONSERVER_ModelBatchFlag:
    __members__: ClassVar[dict] = ...  # read-only
    FIRST_DIM: ClassVar[TRITONSERVER_ModelBatchFlag] = ...
    UNKNOWN: ClassVar[TRITONSERVER_ModelBatchFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_ModelControlMode:
    __members__: ClassVar[dict] = ...  # read-only
    EXPLICIT: ClassVar[TRITONSERVER_ModelControlMode] = ...
    NONE: ClassVar[TRITONSERVER_ModelControlMode] = ...
    POLL: ClassVar[TRITONSERVER_ModelControlMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_ModelIndexFlag:
    __members__: ClassVar[dict] = ...  # read-only
    READY: ClassVar[TRITONSERVER_ModelIndexFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_ModelTxnPropertyFlag:
    __members__: ClassVar[dict] = ...  # read-only
    DECOUPLED: ClassVar[TRITONSERVER_ModelTxnPropertyFlag] = ...
    ONE_TO_ONE: ClassVar[TRITONSERVER_ModelTxnPropertyFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_Parameter:
    @overload
    def __init__(self, arg0: str, arg1: bytes) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: bool) -> None: ...

class TRITONSERVER_ParameterType:
    __members__: ClassVar[dict] = ...  # read-only
    BOOL: ClassVar[TRITONSERVER_ParameterType] = ...
    BYTES: ClassVar[TRITONSERVER_ParameterType] = ...
    INT: ClassVar[TRITONSERVER_ParameterType] = ...
    STRING: ClassVar[TRITONSERVER_ParameterType] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_RateLimitMode:
    __members__: ClassVar[dict] = ...  # read-only
    EXEC_COUNT: ClassVar[TRITONSERVER_RateLimitMode] = ...
    OFF: ClassVar[TRITONSERVER_RateLimitMode] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_RequestFlag:
    __members__: ClassVar[dict] = ...  # read-only
    SEQUENCE_END: ClassVar[TRITONSERVER_RequestFlag] = ...
    SEQUENCE_START: ClassVar[TRITONSERVER_RequestFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_RequestReleaseFlag:
    __members__: ClassVar[dict] = ...  # read-only
    ALL: ClassVar[TRITONSERVER_RequestReleaseFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_ResponseAllocator:
    @overload
    def __init__(
        self,
        alloc_function: Callable[
            [object, str, int, TRITONSERVER_MemoryType, int, object],
            Tuple[int, object, TRITONSERVER_MemoryType, int],
        ],
        release_function: Callable[
            [object, int, object, int, TRITONSERVER_MemoryType, int], None
        ],
        start_function: Callable[[object, object], None],
    ) -> None: ...
    @overload
    def __init__(
        self,
        alloc_function: Callable[
            [object, str, int, TRITONSERVER_MemoryType, int, object],
            Tuple[int, object, TRITONSERVER_MemoryType, int],
        ],
        release_function: Callable[
            [object, int, object, int, TRITONSERVER_MemoryType, int], None
        ],
    ) -> None: ...
    def set_buffer_attributes_function(
        self,
        buffer_attributes_function: Callable[
            [object, str, object, object, object], object
        ],
    ) -> None: ...
    def set_query_function(
        self,
        query_function: Callable[
            [object, object, str, Optional[int], TRITONSERVER_MemoryType, int],
            Tuple[TRITONSERVER_MemoryType, int],
        ],
    ) -> None: ...

class TRITONSERVER_ResponseCompleteFlag:
    __members__: ClassVar[dict] = ...  # read-only
    FINAL: ClassVar[TRITONSERVER_ResponseCompleteFlag] = ...
    __entries: ClassVar[dict] = ...
    def __init__(self, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

class TRITONSERVER_Server:
    def __init__(self, arg0: TRITONSERVER_ServerOptions) -> None: ...
    @overload
    def infer_async(
        self, arg0: TRITONSERVER_InferenceRequest, arg1: TRITONSERVER_InferenceTrace
    ) -> None: ...
    @overload
    def infer_async(self, arg0: TRITONSERVER_InferenceRequest) -> None: ...
    def is_live(self) -> bool: ...
    def is_ready(self) -> bool: ...
    def load_model(self, arg0: str) -> None: ...
    def load_model_with_parameters(
        self, arg0: str, arg1: List[TRITONSERVER_Parameter]
    ) -> None: ...
    def metadata(self) -> TRITONSERVER_Message: ...
    def metrics(self) -> TRITONSERVER_Metrics: ...
    def model_batch_properties(self, arg0: str, arg1: int) -> Tuple[int, int]: ...
    def model_config(self, arg0: str, arg1: int, arg2: int) -> TRITONSERVER_Message: ...
    def model_index(self, arg0: int) -> TRITONSERVER_Message: ...
    def model_is_ready(self, arg0: str, arg1: int) -> bool: ...
    def model_metadata(self, arg0: str, arg1: int) -> TRITONSERVER_Message: ...
    def model_statistics(self, arg0: str, arg1: int) -> TRITONSERVER_Message: ...
    def model_transaction_properties(self, arg0: str, arg1: int) -> Tuple[int, int]: ...
    @overload
    def poll_model_repository(self) -> None: ...
    @overload
    def poll_model_repository(self) -> None: ...
    def register_model_repository(
        self, arg0: str, arg1: List[TRITONSERVER_Parameter]
    ) -> None: ...
    def stop(self) -> None: ...
    def unload_model(self, arg0: str) -> None: ...
    def unload_model_and_dependents(self, arg0: str) -> None: ...
    def unregister_model_repository(self, arg0: str) -> None: ...

class TRITONSERVER_ServerOptions:
    def __init__(self) -> None: ...
    def add_rate_limiter_resource(self, arg0: str, arg1: int, arg2: int) -> None: ...
    def set_backend_config(self, arg0: str, arg1: str, arg2: str) -> None: ...
    def set_backend_directory(self, arg0: str) -> None: ...
    def set_buffer_manager_thread_count(self, arg0: int) -> None: ...
    def set_cache_config(self, arg0: str, arg1: str) -> None: ...
    def set_cache_directory(self, arg0: str) -> None: ...
    def set_cpu_metrics(self, arg0: bool) -> None: ...
    def set_cuda_memory_pool_byte_size(self, arg0: int, arg1: int) -> None: ...
    def set_exit_on_error(self, arg0: bool) -> None: ...
    def set_exit_timeout(self, arg0: int) -> None: ...
    def set_gpu_metrics(self, arg0: bool) -> None: ...
    def set_host_policy(self, arg0: str, arg1: str, arg2: str) -> None: ...
    def set_log_error(self, arg0: bool) -> None: ...
    def set_log_file(self, arg0: str) -> None: ...
    def set_log_format(self, arg0: TRITONSERVER_LogFormat) -> None: ...
    def set_log_info(self, arg0: bool) -> None: ...
    def set_log_verbose(self, arg0: int) -> None: ...
    def set_log_warn(self, arg0: bool) -> None: ...
    def set_metrics(self, arg0: bool) -> None: ...
    def set_metrics_config(self, arg0: str, arg1: str, arg2: str) -> None: ...
    def set_metrics_interval(self, arg0: int) -> None: ...
    def set_min_supported_compute_capability(self, arg0: float) -> None: ...
    def set_model_control_mode(self, arg0: TRITONSERVER_ModelControlMode) -> None: ...
    def set_model_load_device_limit(
        self, arg0: TRITONSERVER_InstanceGroupKind, arg1: int, arg2: float
    ) -> None: ...
    def set_model_load_thread_count(self, arg0: int) -> None: ...
    def set_model_namespacing(self, arg0: bool) -> None: ...
    def set_model_repository_path(self, arg0: str) -> None: ...
    def set_pinned_memory_pool_byte_size(self, arg0: int) -> None: ...
    def set_rate_limiter_mode(self, arg0: TRITONSERVER_RateLimitMode) -> None: ...
    def set_repo_agent_directory(self, arg0: str) -> None: ...
    def set_response_cache_byte_size(self, arg0: int) -> None: ...
    def set_server_id(self, arg0: str) -> None: ...
    def set_startup_model(self, arg0: str) -> None: ...
    def set_strict_model_config(self, arg0: bool) -> None: ...
    def set_strict_readiness(self, arg0: bool) -> None: ...

class TritonError(Exception): ...
class UnavailableError(TritonError): ...
class UnknownError(TritonError): ...
class UnsupportedError(TritonError): ...

def TRITONSERVER_DataTypeByteSize(arg0: TRITONSERVER_DataType) -> int: ...
def TRITONSERVER_DataTypeString(arg0: TRITONSERVER_DataType) -> str: ...
def TRITONSERVER_InferenceTraceActivityString(
    arg0: TRITONSERVER_InferenceTraceActivity,
) -> str: ...
def TRITONSERVER_InferenceTraceLevelString(
    arg0: TRITONSERVER_InferenceTraceLevel,
) -> str: ...
def TRITONSERVER_InstanceGroupKindString(
    arg0: TRITONSERVER_InstanceGroupKind,
) -> str: ...
def TRITONSERVER_LogIsEnabled(arg0: TRITONSERVER_LogLevel) -> bool: ...
def TRITONSERVER_LogMessage(
    arg0: TRITONSERVER_LogLevel, arg1: str, arg2: int, arg3: str
) -> None: ...
def TRITONSERVER_MemoryTypeString(arg0: TRITONSERVER_MemoryType) -> str: ...
def TRITONSERVER_ParameterTypeString(arg0: TRITONSERVER_ParameterType) -> str: ...
def TRITONSERVER_StringToDataType(arg0: str) -> TRITONSERVER_DataType: ...
def api_version() -> tuple: ...