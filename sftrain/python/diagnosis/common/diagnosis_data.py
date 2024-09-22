from abc import ABCMeta, abstractmethod
from datetime import datetime
from typing import List, Optional


class DiagnosisDataType:
    CUDALOG = "cuda_log"
    TRAININGLOG = "training_log"
    CHIPMETRICES = "chip_metrics"


class DiagnosisData(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def get_timestamp(self) -> float:
        pass

    @abstractmethod
    def get_type(self) -> str:
        pass


class CudaLog(DiagnosisData):
    def __init__(self, timestamp: int):
        if timestamp == 0:
            self.timestamp = int(round(datetime.now().timestamp()))
        else:
            self.timestamp = timestamp

    def get_timestamp(self) -> int:
        return self.timestamp

    def get_type(self) -> str:
        return DiagnosisDataType.CUDALOG


class TrainingLog(DiagnosisData):
    def __init__(self, timestamp: int = 0, logs: List[str] = None):
        super().__init__()
        if timestamp == 0:
            self.timestamp = int(round(datetime.now().timestamp()))
        else:
            self.timestamp = timestamp
        self.logs: Optional[List[str]] = logs

    def get_timestamp(self) -> int:
        return self.timestamp

    def get_type(self) -> str:
        return DiagnosisDataType.TRAININGLOG


class ChipMetrics(DiagnosisData):
    def __init__(self, timestamp: int):
        if timestamp == 0:
            self.timestamp = int(round(datetime.now().timestamp()))
        else:
            self.timestamp = timestamp

    def get_timestamp(self) -> int:
        return self.timestamp

    def get_type(self) -> str:
        return DiagnosisDataType.CHIPMETRICES
