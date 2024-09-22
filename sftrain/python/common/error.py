from dataclasses import dataclass
from typing import Any

from sftrain.python.common.serialize import JsonSerializable


@dataclass
class ProcessError(JsonSerializable):
    local_rank: int
    exitcode: int
    message: str
    datetime: Any
