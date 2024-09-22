from torch.distributed.elastic.agent.server.api import RunResult, WorkerSpec


class WorkerContext:
    def __init__(
        self,
        worker_spec: WorkerSpec,
        remaining_failovers: int,
        restart_count: int,
        run_result: RunResult,
    ):
        self._worker_spec: WorkerSpec = worker_spec
        self.remaining_failovers = remaining_failovers
        self.restart_count = restart_count
        self._run_result = run_result

    @property
    def worker_spec(self):
        return self._worker_spec

    @property
    def run_result(self):
        return self._run_result

    def to_string(self) -> str:
        return (
            "WorkerContext:\n"
            f"worker_spec: {self._worker_spec}\n"
            f"remaining_failover: {self.remaining_failovers}\n"
            f"restart_count: {self.restart_count}\n"
            f"run_result: {self._run_result}"
        )
